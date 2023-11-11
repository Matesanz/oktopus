<script lang="ts">
	import DocNode from '$lib/components/DocNode.svelte';
	import { onMount } from 'svelte';
	import { Node, Svelvet, Minimap, Controls } from 'svelvet';
	import type { NodeInfo } from '$lib/types';
	import { get_all_documents, post_query } from '$lib/api';

	let query = '';
	let move_down = false;
	let nodes: NodeInfo[] = [];
	let matches: number[] = [];

	onMount(async () => {
		nodes = await get_all_documents();
	});

	async function submit() {
		matches = await post_query(query);
		move_down = true;
		// window.alert(`API call with query: ${query} ${move_down}`);
	}
</script>

<section class="hero is-fullheight-with-navbar">
	<div class="hero-head">
		<nav class="navbar is-primary has-background-primary" aria-label="main navigation">
			<a class="navbar-item" href="https://bulma.io">
				<img src="/icon.png" height="28" alt="A" />
			</a>
			<div class="navbar-brand">
				<a class="navbar-item" href="/"> OKTOPUS </a>
			</div>
		</nav>
	</div>
	<div
		class="hero-body {move_down ? 'is-align-items-end' : ''}"
		style="transition: 1s ease-in-out;"
	>
		<div class="container is-centered has-text-centered">
			<h1 class="title">Oktopus</h1>
			<div class="columns is-centered to-bottom">
				<div class="column is-three-fifths is-justify-content-center">
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
</section>

<Svelvet height={512}>
	{#each nodes as node}
		<DocNode {node} selected={matches.includes(node.id)} />
	{/each}
</Svelvet>
