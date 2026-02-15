<script lang="ts">
	import type { LangItem } from '$lib/types/LangItem';
	import type { MouseEventHandler } from 'svelte/elements';

	type Props = {
		item: LangItem;
		onNext: MouseEventHandler<HTMLButtonElement>;
	};
	let { item, onNext }: Props = $props();

	let flipped = $state(false);

	// TODO: state could be handled outside this component easily
	function onNextInternal(e: any) {
		flipped = false;
		onNext(e);
	}

	function showAnswer() {
		flipped = true;
	}
</script>

<div id="card" class="">
	<div id="translated" class="mc-font text-center text-xl">
		{item.translated}
	</div>
	<div id="original" class="{flipped ? '' : 'collapse'} text-center text-xl">
		{item.original}
	</div>
	<div
		id="key"
		class="{flipped
			? ''
			: 'collapse'}  font-weight-semibold text-center text-gray-600"
	>
		{item.key}
	</div>
</div>
<div id="controls" class="text-center">
	<button onclick={showAnswer} class="m-1 p-1 outline-2">Show</button>
	<button onclick={onNextInternal} class="m-1 p-1 outline-2">Next</button>
</div>
