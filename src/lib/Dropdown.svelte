<script lang="ts">
	// default to values to contents if not specified
	interface DropdownProps {
		contents: string[];
		values?: string[] | null; // TODO: this is kinda sloppy tbh
		value: string;
		id: string;
	}
	let {
		contents,
		values = null,
		value = $bindable(),
		id
	}: DropdownProps = $props();
</script>

<select bind:value {id} class="m-1 px-2 py-1 outline-2">
	{#each contents as content, i}
		<option value={values === null ? content : values[i]}>
			{content}
		</option>
	{/each}
</select>

<style>
	select {
        background-color: var(--bg-color);
        outline-color: var(--outline-color);
        outline-width: var(--outline-width);
	}
</style>
