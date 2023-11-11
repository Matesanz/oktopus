<script>
	import { onMount } from 'svelte';
	import { Node, Svelvet, Minimap, Controls } from 'svelvet';
	import DocNode from '$lib/components/DocNode.svelte';

	const API_URL = '127.0.0.1';
	let query = '';

	let documents = [];
	let best;
	onMount(async () => {
		documents = await get_documents();
	});

	async function get_documents() {
		alert(`beep bop beep.... GET!`);
		return [1, 2, 3, 4, 5, 6];
	}

	async function send_query() {
		alert(`beep bop beep.... \`${query}\``);
		return [2, 4, 6];
	}
</script>

<section class="hero is-fullheight">
	<div class="hero-body">
		<div class="container has-text-centered">
			<h1 class="title">Oktopus</h1>
			<div class="field has-addons">
				<div class="control">
					<input
						class="input"
						type="text"
						placeholder="Look for insight"
						bind:value={query}
						on:keydown={(e) => {
							if (e.key == 'Enter') {
								best = send_query();
							}
						}}
					/>
				</div>
				<div class="control">
					<button class="button is-info is-bold" on:click={send_query}>Search</button>
				</div>
			</div>
		</div>
	</div>
</section>

chart:
<Svelvet id="my-canvas" width={500} height={500} TD minimap locked>
	<DocNode title="esta" x={0} y={0} />
	<DocNode title="prohibido" x={64} y={64} />
	<DocNode title="pushear" x={128} y={256} />
	<DocNode title="main" x={256} y={256} />
</Svelvet>
end
