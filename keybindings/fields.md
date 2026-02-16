# Keybindings - Field Structure

This note type stores keybinding prompts and answers with the following field structure:

## Fields

1. **Effect** - What the keybinding does (e.g., `new window`, `save file`)
2. **Binding** - The key sequence or command (e.g., `<C-b> c`, `:w`)
3. **Program** - Where the keybinding applies (e.g., `tmux`, `nvim normal mode`)

## Format

Each note follows the pipe-delimited format:
```
Effect|Binding|Program
```

## Example

```
new window|<C-b> c|tmux
save|:w|nvim commands
open telescope file finder|<leader>ff|nvim normal mode
```

## Notes

- Keep fields in this exact order: `Effect|Binding|Program`
- Use one note per keybinding
- Keep binding text exactly as you use it in practice
