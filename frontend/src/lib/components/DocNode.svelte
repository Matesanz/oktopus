<script lang="ts">
	import { get_document_info } from '$lib/api';
	import { Node } from 'svelvet';
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	export let node: Node;
	export let selected: boolean = false;

	function scale(x: number, k = 300) {
		return x * k;
	}

	async function handle_click() {
		let { content } = await get_document_info(node.id);
		dispatch('message', {
			modalActive: true
		});
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
		<div class="marker {selected ? 'selected' : 'not-selected'}" />
		<h1 class="subtitle has-text-centered">{node.title}</h1>
	</Node>
</div>

<style>
	.marker {
		width: 100px;
		height: 100px;
		border-radius: 50%;
	}

	.selected {
		background-color: #dd57ff;
	}

	.not-selected {
		background-color: #ffdd57;
	}
</style>
