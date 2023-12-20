function flipPancake(level, pancakeSizes, pancakeElement) {
    const adjustedPancakeSizes = pancakeSizes.map(size => size);

    fetch(`/flip_pancakes/${level}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(adjustedPancakeSizes)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);

        if ('flips' in data && data.flips.length > 0) {
            const flipsNeeded = data.flips;
            console.log(`Flips needed: ${flipsNeeded}`);
            document.getElementById('message').innerText = `Flips needed: ${flipsNeeded}`;

            // Apply flipping animation
            const pancakesToFlip = document.querySelectorAll('.pancake-stack .pancake');
            pancakesToFlip.forEach((pancake, index) => {
                pancake.classList.add('flip');
                pancake.addEventListener('transitionend', () => {
                    pancake.classList.remove('flip');
                    // Check if this is the last pancake in the loop
                    if (index === pancakesToFlip.length - 1) {
                        // Wait for the flipping animation to complete
                        setTimeout(() => {
                            // Show sorted pancakes
                            document.getElementById('message').innerText = 'Pancakes Sorted';
                        }, 500); // Adjust the timing based on your animation speed
                    }
                }, { once: true });
            });
        } else if ('message' in data && data.message.includes('completed')) {
            // Handle completion scenario
            document.getElementById('message').innerText = 'Level Completed';
        } else if ('message' in data && data.message.includes('sorted')) {
            // Handle sorted scenario
            document.getElementById('message').innerText = 'Pancakes Sorted';
        } else {
            // Handle other scenarios or errors
            document.getElementById('message').innerText = 'Error';
        }
    });
}
