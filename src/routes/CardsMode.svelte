<script lang="ts">
	import Card from './Card.svelte';
	import type { LangItem } from '$lib/types/LangItem';
	import type { Dictionary } from '$lib/types/Dictionary';
	import engLangDataTemp from '$lib/data/en_gb.json';
	import type { Category } from '$lib/types/Category';
	import { shuffleArray, randIndex } from '$lib/utils';

	const engLangData: Dictionary<string> = engLangDataTemp;

	type CardModeOptions = {
		infinite: boolean;
		uselessChance: number;
	};
	type Props = {
		categoryData: Category;
		translatedLangData: Dictionary<string>;
		options: CardModeOptions;
	};
	let { categoryData, translatedLangData, options }: Props = $props();

	let itemGenerator: Generator<LangItem> | null = $state(null);

	$effect(() => {
		itemGenerator = genItem(
			categoryData,
			engLangData,
			translatedLangData,
			options
		);
	});

	let currItem: LangItem | null = $state(null);
	$effect(() => {
		if (itemGenerator !== null) {
			currItem = itemGenerator.next().value;
		}
	});

	// $inspect(categoryData).with(console.log);

	function nextItem() {
		if (itemGenerator !== null) {
			currItem = itemGenerator.next().value;
		}
	}

	function* genItem(
		categoryData: Category,
		engLangData: Dictionary<string>,
		translatedLangData: Dictionary<string>,
		options: CardModeOptions
	): Generator<LangItem> {
		const keys: string[] = categoryData.useful.slice();
		if (categoryData.other.length > 0) {
			for (let i = 0; i < options.uselessChance; i++) {
				const r: number = randIndex(categoryData.other)!!;
				keys.push(categoryData.other[r]);
			}
		}
		shuffleArray(keys);
		while (options.infinite) {
			for (let i = 0; i < keys.length; i++) {
				let currKey: string = keys[i];
				const item: LangItem = {
					key: currKey,
					translated: translatedLangData[currKey] ?? engLangData[currKey],
					original: engLangData[currKey]
				};
				yield item;
			}
		}
	}
</script>

<p>
	{options.infinite ? 'Infinite mode' : 'Not infinite mode'}
</p>
<p>
	Useless chance: {options.uselessChance} / {categoryData.useful.length}
</p>

{#if currItem !== null}
	<Card item={currItem} onNext={nextItem} />
{/if}
