<script lang="ts">
	import Dropdown from '$lib/Dropdown.svelte';
    import type { Dictionary } from '$lib/types/Dictionary';
	import type { Category } from '$lib/types/Category';

	type Props = {
		selectedLangName: string;
		langNames: string[];
		selectedMode: string;
		selectedCategoryId: string;
		categories: Dictionary<Category>;
	};
	let {
		selectedLangName = $bindable(),
		langNames,
		selectedMode = $bindable(),
		selectedCategoryId = $bindable(),
		categories
	}: Props = $props();
</script>

<div
	class="inline-block w-full content-center border-2 bg-indigo-200
    p-2"
>
	<label for="lang-select">Language: </label>
	<Dropdown
		id="lang-select"
		bind:value={selectedLangName}
		contents={langNames}
		--outline-width="2px"
		--bg-color="var(--color-violet-200)"
	/>
	<label for="mode-select">mode: </label>
	<Dropdown
		id="mode-select"
		bind:value={selectedMode}
		contents={['cards', 'quiz', 'look']}
		--outline-width="2px"
		--bg-color="var(--color-violet-200)"
	/>
	<label for="category-select">Category: </label>
	<Dropdown
		id="category-select"
		bind:value={selectedCategoryId}
		values={Object.keys(categories)}
		contents={Object.values(categories).map((it) => it.name)}
		--outline-width="2px"
		--bg-color="var(--color-violet-200)"
	/>
	<button class="bg-violet-200 px-[9px] py-[2px] outline-2"> + </button>
</div>
