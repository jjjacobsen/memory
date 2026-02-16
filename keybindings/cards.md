# Keybindings - Card Templates

This note type has two card templates.

## 1. Program+Effect -> Program+Effect+Binding

### Front
```
<b>Program:</b> {{Program}}<br>
<b>Effect:</b> {{Effect}}<br>
<hr>
What is the keybinding?
```

### Back
```
{{FrontSide}}

<hr id=answer>

<b>Binding:</b> {{Binding}}
```

## 2. Program+Binding -> Program+Binding+Effect

### Front
```
<b>Program:</b> {{Program}}<br>
<b>Binding:</b> {{Binding}}<br>
<hr>
What does this keybinding do?
```

### Back
```
{{FrontSide}}

<hr id=answer>

<b>Effect:</b> {{Effect}}
```

## Notes

- Card 1 tests recall from effect to binding
- Card 2 tests recall from binding to effect
- Use the same three fields for both cards: `Effect`, `Binding`, `Program`
