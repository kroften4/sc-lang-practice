<script lang="ts">
	import langList from '$lib/data/langlist.json';
	import engLangDataTemp from '$lib/data/en_gb.json';
	import categoriesData from '$lib/data/categories.json';
	import ItemSearch from './ItemSearch.svelte';
	import type { Dictionary } from '$lib/types/Dictionary';
	import { onMount } from 'svelte';
	import CardsMode from './CardsMode.svelte';
	import type { Category } from '$lib/types/Category';
	import SettingsBar from './SettingsBar.svelte';

	const engLangData: Dictionary<string> = engLangDataTemp;

	const langNames = langList.map((name: string) => name.split('.')[0]).sort();
	const translationKeys = Object.keys(engLangData);

	prepareCategories(categoriesData);
	let categories: Dictionary<Category> = $state(categoriesData);

	onMount(loadLang);

	let selectedLangName = $state(langNames[0]);
	let selectedLangData = $state(null);

	$effect(loadLang);

	type Mode = 'cards' | 'quiz' | 'look';
	let selectedMode: Mode = $state('cards');

	let selectedCategoryId: string = $state(Object.keys(categories)[0]);
	let selectedCategory: Category = $derived(categories[selectedCategoryId]);

	let searchTerm = '';

	function loadLang() {
		fetch(`/langfiles/${selectedLangName}.json`)
			.then((r) => r.json())
			.then((r) => {
				selectedLangData = r;
			});
		return;
	}

	function prepareCategories(dict: Dictionary<Category>) {
		for (let category in dict) {
			let usefulSet = prepareCategoryList(dict[category].useful);
			dict[category].useful = Array.from(usefulSet);

			let otherSet = prepareCategoryList(dict[category].other);
			dict[category].other = Array.from(otherSet.difference(usefulSet));
		}
	}

	function prepareCategoryList(list: string[]): Set<string> {
		let result: Set<string> = new Set();
		for (let item of list) {
			if (translationKeys.includes(item)) {
				result.add(item);
				continue;
			}
			// abc.dbe.* -> abc.dbe.item
			// TODO: handle * in the middle
			if (item.endsWith('*')) {
				let term = item.slice(0, -1);
				let filtered = translationKeys.filter((it) => it.startsWith(term));
				result = result.union(new Set(filtered));
			} else {
				console.warn(`${item} not found`);
			}
		}
		return result;
	}
</script>

<h1 class="m-2 text-center text-3xl font-bold">
	Search Crafting Language Learning
</h1>

<SettingsBar
	bind:selectedLangName
	{langNames}
	bind:selectedMode
	bind:selectedCategoryId
	{categories}
/>

{#if selectedLangData}
	{#if selectedMode === 'cards'}
		<CardsMode translatedLangData={selectedLangData} />
	{:else if selectedMode === 'quiz'}
		<div>Nothing yet</div>
	{:else if selectedMode === 'look'}
		<ItemSearch langData={selectedLangData} {engLangData} />
	{/if}
{/if}

<style>
	:root {
		margin: 5px;
		background-color: var(--color-violet-100);
	}

	:global {
		@font-face {
			font-family: Minecraft;
			size-adjust: 130%;
			src: url(/fonts/MinecraftDefault-Regular.ttf);
		}
		@font-face {
			font-family: 'GNU Unifont';
			src: url(/fonts/unifont-17.0.03.otf);
		}
		@font-face {
			font-family: 'GNU Unifont Japanese';
			src: url(/fonts/unifont_jp-17.0.03.otf);
		}
		.mc-font {
			font-family: Minecraft, 'GNU Unifont', 'GNU Unifont Japanese';
		}
	}
</style>
