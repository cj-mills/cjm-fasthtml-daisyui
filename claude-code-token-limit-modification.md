# Modifying Claude Code File Reading Token Limit

## Overview
Claude Code has a built-in limit of 25,000 tokens when reading files. This limit can be modified by editing the installed npm package files.

## Location
The token limit is defined in the Claude Code CLI JavaScript file:
```
/home/innom-dt/.claude/local/node_modules/@anthropic-ai/claude-code/cli.js
```

## Finding the Limit
Search for the following pattern in the file:
```javascript
var RSB=25000;
```

This variable `RSB` defines the maximum number of tokens allowed when reading files.

## Modifying the Limit
1. Open the file in a text editor with appropriate permissions
2. Search for `RSB=25000`
3. Change `25000` to your desired token limit (e.g., `50000` for double the limit)
4. Save the file

## Important Notes
- **This is a temporary solution**: The change will be overwritten when Claude Code is updated
- **Location line number**: As of the current version, the limit is around line 1549
- **Error message**: The limit is referenced in error messages like:
  ```
  File content (31493 tokens) exceeds maximum allowed tokens (25000)
  ```

## Related Code Context
The limit is used in the file reading logic where it checks token counts before allowing file content to be returned. The error class `nb1` (MaxFileReadTokenExceededError) is thrown when this limit is exceeded.

## Alternative Solutions
If you prefer not to modify the installed package:
1. Use the `offset` and `limit` parameters when reading large files
2. Use the Grep tool to search for specific content
3. Split large files into smaller chunks
4. Request a feature for configurable limits in the official Claude Code repository

## Verification
After making the change, you can verify it works by attempting to read a file that previously exceeded the 25,000 token limit.