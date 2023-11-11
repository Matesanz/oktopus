<script lang="ts">
	import DocNode from '$lib/components/DocNode.svelte';
	import SvelteMarkdown from 'svelte-markdown';
	import { onMount } from 'svelte';
	import { Svelvet } from 'svelvet';
	import type { NodeInfo } from '$lib/types';
	import { api_url, get_all_documents, post_query } from '$lib/api';
	import { fly } from 'svelte/transition';

	let query = '';
	let show_graph = false;
	let nodes: NodeInfo[] = [];
	let matches: NodeInfo[] = [];
	let modal_open: boolean = false;
	let modal_title: string = '';
	let modal_content: string = '';
	let modal_chunk: string = '';

	function clear_modal() {
		modal_title = '';
		modal_content = '';
		modal_chunk = '';
		modal_open = false;
	}

	onMount(async () => {
		nodes = await get_all_documents();
	});

	async function submit() {
		matches = await post_query(query);
		show_graph = true;
		// window.alert(`API call with query: ${query} ${show_graph}`);
	}
</script>

<div class="modal {modal_open ? 'is-active' : ''}">
	<div class="modal-background" />
	<div class="modal-card">
		<header class="modal-card-head">
			<p class="modal-card-title">{modal_title}</p>
			<button class="delete" aria-label="close" on:click={clear_modal} />
		</header>
		<section class="modal-card-body">
			{#if modal_chunk.length > 0}
				<article class="message is-info">
					<div class="message-header">
						<p>Insight</p>
					</div>
					<div class="message-body">
						{modal_chunk}
					</div>
				</article>
			{/if}
			<hr />
			<SvelteMarkdown source={modal_content} />
		</section>
		<footer class="modal-card-foot">
			<button class="button is-black is-fullwidth" on:click={clear_modal}>Close</button>
		</footer>
	</div>
</div>

<main class="main">
	<section class="hero is-medium {show_graph ? 'mb-8' : ''}">
		<div class="hero-head">
			<nav class="navbar has-shadow" aria-label="main navigation">
				<div class="navbar-brand">
					<a
						class="navbar-item"
						href="/"
						on:click={(_) => {
							show_graph = false;
							query = '';
						}}
					>
						<i class="fa-brands fa-octopus-deploy" />
						<b class="ml-2"> OKTOPUS </b>
					</a>
				</div>
				<div id="navbar-stuff" class="navbar-menu">
					<div class="navbar-end">
						<a class="navbar-item" href="{api_url}/docs" target="_blank"> API </a>
						<a class="navbar-item" href="{api_url}/redoc" target="_blank"> Documentation </a>
					</div>
				</div>
			</nav>
		</div>
		<div
			class={show_graph ? 'is-align-items-end p-4' : 'hero-body'}
			style="transition: 1s ease-in-out;"
		>
			<div class="container is-fluid">
				{#if show_graph}
					<div class="mb-4" in:fly>
						<Svelvet height={window.innerHeight * 0.75}>
							{#each nodes as node}
								<DocNode
									{node}
									selected={matches.some((n) => n.id == node.id)}
									on:message={(event) => {
										let { title, content } = event.detail;
										modal_content = content;
										modal_title = title;
										// get the chunk from the corresponding match
										const matching_node = matches.find((n) => n.id == node.id);
										if (matching_node) {
											modal_chunk = matching_node.chunk;
										} else {
											modal_chunk = '';
										}
										modal_open = true;
									}}
								/>
							{/each}
						</Svelvet>
					</div>
				{/if}
				<div class="is-centered has-text-centered">
					{#if !show_graph}
						<h1 class="title">OKTOPUS</h1>
						<h2 class="subtitle">Discover insight in a sea of uncertainty</h2>
					{/if}
					<div class="columns is-centered to-bottom">
						<div class="column {show_graph ? '' : 'is-three-fifths'} is-justify-content-center">
							<div class="field has-addons is-justify-content-center">
								<div class="control is-expanded">
									<input
										class="input is-black"
										type="text"
										placeholder="Look for insight"
										bind:value={query}
										on:keydown={(e) => {
											if (e.key === 'Enter' && query.length > 0) {
												submit();
											}
										}}
									/>
								</div>
								<div class="control">
									<button
										class="button is-black is-rounded"
										on:click={() => submit()}
										disabled={query.length === 0}
										>Ask <i class="ml-2 fa-solid fa-arrow-right" /></button
									>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>
	<footer class="mt-{show_graph ? '8' : '2'} py-4 has-text-light has-background-info">
		<div class="has-text-centered">
			<p>
				<i class="fa-brands fa-octopus-deploy" />
				OKTOPUS by Move 38 with ❤️ for JUNCTION.
			</p>
		</div>
	</footer>
</main>

<style>
	.main {
		display: flex;
		min-height: 100vh;
		flex-direction: column;
	}

	.hero {
		flex: 1;
	}
</style>
