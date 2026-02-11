<script lang="ts">
	// default to values to contents if not specified
	interface DropdownProps {
		contents: string[];
        values?: string[] | null; // TODO: this is kinda sloppy tbh
		value: string;
		id: string;
	}
	let { contents, values = null, value = $bindable(), id }: DropdownProps = $props();
</script>

<select bind:value {id}>
	{#each contents as content, i}
		<option value={values === null ? content : values[i]}>
			{content}
		</option>
	{/each}
</select>

<style>
	select {
		outline: 2px solid black;
		padding: 5px 8px;
		margin: 3px;
	}
</style>
