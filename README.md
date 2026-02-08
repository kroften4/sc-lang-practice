currently using https://github.com/toxicity188/all-minecraft-language

# TODO
- minecraft font
- figure out where and how to download all language files for each version

## UX
- honestly this could be really similar to monkeytype
- save/load custom selection
- load language file
- 2 lists (useful, other) for each category

options: 
- load language (name, mc version)
- include only useful / include all
- category select
- mode select

categories:
- subtitles
- enchantments
  - levels
  - names
  - both
- advancements
- biome (exclude minecraft.banner)
- difficulty
- bar (sleep)
- custom (work on convenient selection, maybe buttons to select everything from
  a predefined category, somehow mask select like `biome.minecraft.*`)

modes:
- like language-learning cards: show a question, flip to check your answer
- type in an answer (search) / select it (for categories with few options)

# sv

Everything you need to build a Svelte project, powered by [`sv`](https://github.com/sveltejs/cli).

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```sh
# create a new project
npx sv create my-app
```

To recreate this project with the same configuration:

```sh
# recreate this project
bun x sv create --template minimal --types ts --add prettier eslint tailwindcss="plugins:none" --install bun ./
```

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```sh
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```sh
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.
