<script lang="ts">
	import Card from './Card.svelte';
	import type { LangItem } from '$lib/types/LangItem';
	import type { Dictionary } from '$lib/types/Dictionary';
	import engLangDataTemp from '$lib/data/en_gb.json';

	function shuffleArray(arr: any[]): any[] {
		return arr.toSorted(function (a, b) {
			return Math.random() - 0.5;
		});
	}

	const engLangData: Dictionary<string> = engLangDataTemp;

	let { translatedLangData } = $props();

	const keys: string[] = shuffleArray(Object.keys(engLangDataTemp));
	let currIndex: number = 0;
	let selectedKey: string = $state(keys[currIndex]);
	function nextKey() {
		currIndex++;
		selectedKey = keys[currIndex];
	}

	let currItem: LangItem = $derived({
		key: selectedKey,
		translated: translatedLangData[selectedKey] ?? engLangData[selectedKey],
		original: engLangData[selectedKey]
	});

	// function updateCurrItem() {
	// 	currItem = {
	// 		key: selectedKey,
	// 		translated: translatedLangData[selectedKey],
	// 		original: engLangData[selectedKey]
	// 	};
	// }
</script>

<Card item={currItem} onNext={nextKey} />
