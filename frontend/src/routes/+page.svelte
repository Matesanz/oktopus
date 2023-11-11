<script lang="ts">
	import DocNode from '$lib/components/DocNode.svelte';
	import { onMount } from 'svelte';
	import { Node, Svelvet, Minimap, Controls } from 'svelvet';
	import type { NodeInfo } from '$lib/types';
	import { get_all_documents, post_query } from '$lib/api';
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
			{modal_content}
		</section>
		<footer class="modal-card-foot">
			<button class="button is-primary is-fullwidth" on:click={(_) => (modal_open = false)}
				>Close</button
			>
		</footer>
	</div>
</div>

<section class="hero is-large">
	<div class="hero-head">
		<nav class="navbar is-primary has-background-primary" aria-label="main navigation">
			<div class="navbar-brand">
				<a class="navbar-item" href="/">
					<img src="/icon.png" height="28" alt="logo" class="mr-4" />
					<b> OKTOPUS </b>
				</a>
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
					<h1 class="title">Oktopus</h1>
				{/if}
				<div class="columns is-centered to-bottom">
					<div class="column {show_graph ? '' : 'is-three-fifths'} is-justify-content-center">
						<div class="field has-addons is-justify-content-center">
							<div class="control is-expanded">
								<input
									class="input"
									type="text"
									placeholder="Look for insight"
									bind:value={query}
									on:keydown={(e) => {
										if (e.key === 'Enter') {
											submit();
										}
									}}
								/>
							</div>
							<div class="control">
								<button class="button is-bold is-primary is-rounded" on:click={() => submit()}
									>Search</button
								>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>
<footer class="mt-8 footer has-text-light has-background-primary">
	<div class="content has-text-centered">
		<p>
			<strong>Oktopus by Move 38 with ❤️ for JUNCTION</strong>.
		</p>
	</div>
</footer>
