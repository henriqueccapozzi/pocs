#!/bin/bash

function handleSuccess {
	echo "handleSuccess"
	# Checks if there's data in stdin
	if [[ -p /dev/stdin ]]; then
		# Does whatever is desired with the input
		input="$(cat -)"
		echo "handling success for input:"
		echo "$input"
	fi
}

function handleFailure {
	echo "handleFailure"
	# replicate stdin handling if needed
}

stat $1 2>/dev/null >&2 && handleSuccess || handleFailure 
