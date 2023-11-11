<script lang="ts">
	import DocNode from '$lib/components/DocNode.svelte';
	import { Node, Svelvet, Minimap, Controls } from 'svelvet';

	let query: string = '';
	let move_down = false;

	function send_query() {
		alert(`beep bop beep.... \`${query}\``);
	}

	function submit() {
		move_down = true;
		// window.alert(`API call with query: ${query} ${move_down}`);
	}
</script>

<section class="hero is-fullheight">
	<div
		class="hero-body {move_down ? 'is-align-items-end' : ''}"
		style="transition: 1s ease-in-out;"
	>
		<div class="container is-centered has-text-centered">
			<h1 class="title">Oktoopus</h1>
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
	<DocNode
		title="Sample "
		position={{
			x: 100,
			y: 100
		}}
	/>
</Svelvet>
