<script lang="ts">
	import { Node } from 'svelvet';

	export let title: string;
	export let x: number;
	export let y: number;
	export let selected: boolean = false;

	function scale(x: number, k = 300) {
		return x * k;
	}
</script>

<Node
	position={{
		x: scale(x),
		y: scale(y)
	}}
>
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
