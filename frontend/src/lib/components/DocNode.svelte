<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import { get_document_info } from '$lib/api';
	import type { NodeInfo } from '$lib/types';
	import { Node } from 'svelvet';

	export let node: NodeInfo;
	export let selected: boolean = false;

	const dispatch = createEventDispatcher();

	const max_length = 16;
	$: trimmed_title = `${node.title.slice(0, max_length)}${
		node.title.length > max_length ? '...' : ''
	}`;

	function scale(x: number, k = 100) {
		return x * k;
	}

	async function handle_click() {
		let content = await get_document_info(node.id);
		dispatch('message', { title: node.title, content });
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
		title={node.title}
		borderColor={selected ? 'red' : 'black'}
	>
		<div class="marker {selected ? 'selected' : 'not-selected'}" />
		<p class="ml-2">{trimmed_title}</p>
	</Node>
</div>
