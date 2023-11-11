<script lang="ts">
	import { get_document_info } from '$lib/api';
	import type { NodeInfo } from '$lib/types';
	import { Node } from 'svelvet';

	export let node: NodeInfo;
	export let selected: boolean = false;

	function scale(x: number, k = 200) {
		return x * k;
	}

	async function handle_click() {
		let { content } = await get_document_info(node.id);
		console.log(content);
	}
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div on:click={(_) => handle_click()}>
	<Node
		position={{
			x: scale(node.x),
			y: scale(node.y)
		}}
	>
		<div class="is-flex is-align-items-center">
			<div class="marker {selected ? 'selected' : 'not-selected'}" />
			<p class="has-text-centered ml-2">{node.title}</p>
		</div>
	</Node>
</div>

<style>
	.marker {
		width: 2em;
		height: 2em;
		border-radius: 50%;
	}

	.marker:hover {
		background-color: red;
	}

	.selected {
		background-color: #64737d;
	}

	.not-selected {
		background-color: #070807;
	}
</style>
