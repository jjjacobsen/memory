# U.S. Presidents - Info - Field Structure

This note type contains basic biographical and political information about US presidents with the following field structure:

## Fields

1. **Number** - The presidential number (e.g., "1", "16", "45")
2. **Name** - The president's full name (e.g., "George Washington", "Abraham Lincoln")
3. **Term** - The years in office (e.g., "1789-1797", "1861-1865")
4. **Party** - The political party affiliation (e.g., "Federalist", "Republican", "Democratic")
5. **Portrait** - Image file for the president's portrait (managed in Anki, not version controlled)
6. **State** - The state the president represented or was from (e.g., "Virginia", "Illinois")

## Format

Each note follows the pipe-delimited format:
```
Number|Name|Term|Party|State
```

## Examples

```
1|George Washington|1789-1797|Federalist|Virginia
16|Abraham Lincoln|1861-1865|Republican|Illinois
32|Franklin D. Roosevelt|1933-1945|Democratic|New York
```

## Notes

- Numbers should be simple integers (1, 2, 3, etc.)
- Terms should use the format "YYYY-YYYY" for full terms
- For presidents who died in office or resigned, use the actual end year
- Portrait field contains image filenames but is managed separately in Anki
- State represents the state most associated with the president's political career
- Party names should use their historical names (e.g., "Democratic-Republican", "Whig") 
