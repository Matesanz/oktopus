<script lang="ts">
	import { Node } from 'svelvet';

	export let title: string;
	export let position: { x: number; y: number };
	export let selected: boolean = false;

	function scale(position: any, k = 250) {
		return {
			x: position.x * k,
			y: position.y * k
		};
	}
</script>

<Node position={scale(position)}>
	<div class="marker {selected ? 'selected' : 'not-selected'}" />
	<h1 class="subtitle has-text-centered">{title}</h1>
</Node>

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
