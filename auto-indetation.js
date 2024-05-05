document.addEventListener('DOMContentLoaded', function() {
	let textareas = document.getElementsByTagName('textarea');

	for (let i = 0; i < textareas.length; i++) {
			let editor = textareas[i];

			editor.addEventListener('keydown', function(event) {
					if (event.key === 'Tab') {
							event.preventDefault(); // Prevent default tab behavior
							insertSpaces(editor, 4); // Insert 4 spaces for tab
					} else if (event.key === 'Enter') {
							event.preventDefault(); // Prevent default enter behavior
							handleNewLineIndentation(editor);
					}
			});
	}
});

function insertSpaces(editor, tabSize) {
	let cursorPos = editor.selectionStart;
	let textBeforeCursor = editor.value.substring(0, cursorPos);
	let textAfterCursor = editor.value.substring(cursorPos);
	let spacesToInsert = ' '.repeat(tabSize - (textBeforeCursor.length % tabSize));

	let newText = textBeforeCursor + spacesToInsert + textAfterCursor;
	editor.value = newText;
	editor.setSelectionRange(cursorPos + spacesToInsert.length, cursorPos + spacesToInsert.length);
}

function handleNewLineIndentation(editor) {
	let cursorPos = editor.selectionStart;
	let textBeforeCursor = editor.value.substring(0, cursorPos);
	let lastNewLineIndex = textBeforeCursor.lastIndexOf('\n');
	let currentLine = textBeforeCursor.substring(lastNewLineIndex + 1);
	let nextLineIndent = '';

	// Calculate the current line's indentation
	let match = currentLine.match(/^(\s+)/);
	if (match) {
			nextLineIndent = match[1]; // Keep the same indentation
	}

	// Increase indentation if the line ends with a colon
	if (currentLine.trim().endsWith(':')) {
			nextLineIndent += '    '; // Add four spaces
	}

	let textAfterCursor = editor.value.substring(cursorPos);
	let newText = textBeforeCursor + '\n' + nextLineIndent + textAfterCursor;
	editor.value = newText;
	let newCursorPos = cursorPos + nextLineIndent.length + 1; // Move cursor to the next line after the indent
	editor.setSelectionRange(newCursorPos, newCursorPos);
}