<script lang="ts">
	import DocNode from '$lib/components/DocNode.svelte';
	import { onMount } from 'svelte';
	import { Node, Svelvet, Minimap, Controls } from 'svelvet';
	import type { NodeInfo } from '$lib/types';
	import { api_url, get_all_documents, post_query } from '$lib/api';
	import { fly } from 'svelte/transition';

	let query = '';
	let show_graph = false;
	let nodes: NodeInfo[] = [];
	let matches: number[] = [];
	let modal_open: boolean = false;
	let modal_title: string = '';
	let modal_content: string = '';

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
			<button class="delete" aria-label="close" on:click={(_) => (modal_open = false)} />
		</header>
		<section class="modal-card-body">
			<article class="message is-info">
				<div class="message-header">
					<p>Insight</p>
				</div>
				<div class="message-body">
					Lorem ipsum dolor sit amet, consectetur adipiscing elit. <strong
						>Pellentesque risus mi</strong
					>, tempus quis placerat ut, porta nec nulla. Vestibulum rhoncus ac ex sit amet fringilla.
					Nullam gravida purus diam, et dictum <a>felis venenatis</a> efficitur. Aenean ac
					<em>eleifend lacus</em>, in mollis lectus. Donec sodales, arcu et sollicitudin porttitor,
					tortor urna tempor ligula, id porttitor mi magna a neque. Donec dui urna, vehicula et sem
					eget, facilisis sodales sem.
				</div>
			</article>
			<hr />
			{modal_content}
		</section>
		<footer class="modal-card-foot">
			<button class="button is-black is-fullwidth" on:click={(_) => (modal_open = false)}
				>Close</button
			>
		</footer>
	</div>
</div>

<main class="main">
	<section class="hero is-medium">
		<div class="hero-head">
			<nav class="navbar is-primary has-background-black" aria-label="main navigation">
				<div class="navbar-brand has-background-primary">
					<a
						class="navbar-item"
						href="/"
						on:click={(_) => {
							show_graph = false;
							query = '';
						}}
					>
						<!--
						
						<img src="/icon.png" height="28" alt="logo" class="mr-4" />
					-->
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
									selected={matches.includes(node.id)}
									on:message={(event) => {
										let { title, content } = event.detail;
										modal_content = content;
										modal_title = title;
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
	<footer class="mt-{show_graph ? '8' : '2'} footer has-text-light has-background-black">
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
