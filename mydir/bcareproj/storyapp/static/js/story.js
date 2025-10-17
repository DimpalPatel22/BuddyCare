document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".tab");
    const highlight = document.querySelector(".tabs-highlight");
    const contents = document.querySelectorAll(".content");

    const totalTabs = tabs.length;
    const wrapper = document.querySelector(".tabs-wrapper");

    // Check if a specific tab is requested via URL
    const urlParams = new URLSearchParams(window.location.search);
    const requestedTab = urlParams.get('tab'); // 'general', 'real', 'success', 'volunteer'
    
    // Map tab name to index
    const tabMap = {
    'general': 0,
    'real': 1,
    'success': 2,
    'volunteer': 3
};
    if(requestedTab && tabMap.hasOwnProperty(requestedTab)) {
        const index = tabMap[requestedTab];
    
    // Move capsule highlight
        const wrapperWidth = wrapper.offsetWidth;
        const padding = 4;
        const capsuleWidth = wrapperWidth / totalTabs - 2 * padding;
        highlight.style.width = `${capsuleWidth}px`;
        highlight.style.left = `${index * (wrapperWidth / totalTabs) + padding}px`;

    // Activate tab text
        tabs.forEach(t => t.classList.remove("active"));
        tabs[index].classList.add("active");

    // Show corresponding content
        contents.forEach(c => c.classList.remove("active"));
        contents[index].classList.add("active");

    // Optionally scroll into view
        contents[index].scrollIntoView({behavior: "smooth"});
    }


    tabs.forEach((tab, index) => {
        tab.addEventListener("click", () => {
            // Calculate capsule movement
            // width of each tab inside wrapper minus padding
            const wrapperWidth = wrapper.offsetWidth;
            const padding = 4; // matches CSS padding
            const capsuleWidth = wrapperWidth / totalTabs - 2 * padding;

            highlight.style.width = `${capsuleWidth}px`;
            highlight.style.left = `${index * (wrapperWidth / totalTabs) + padding}px`;

            // Switch active tab text
            tabs.forEach(t => t.classList.remove("active"));
            tab.classList.add("active");

            // Switch active content
            contents.forEach(c => c.classList.remove("active"));
            contents[index].classList.add("active");
        });
    });
    
});

document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".tab");
    const highlight = document.querySelector(".tabs-highlight");
    const contents = document.querySelectorAll(".content");
    const totalTabs = tabs.length;
    const wrapper = document.querySelector(".tabs-wrapper");

    // --- Tab capsule movement ---
    tabs.forEach((tab, index) => {
        tab.addEventListener("click", () => {
            const wrapperWidth = wrapper.offsetWidth;
            const padding = 4;
            const capsuleWidth = wrapperWidth / totalTabs - 2 * padding;

            highlight.style.width = `${capsuleWidth}px`;
            highlight.style.left = `${index * (wrapperWidth / totalTabs) + padding}px`;

            tabs.forEach(t => t.classList.remove("active"));
            tab.classList.add("active");

            contents.forEach(c => c.classList.remove("active"));
            contents[index].classList.add("active");
        });
    });

    // --- Scroll to specific story if ?story= is in URL ---
    const urlParams = new URLSearchParams(window.location.search);
    const storyId = urlParams.get('story');

    if (storyId) {
        // Activate Real Life tab
        tabs.forEach(t => t.classList.remove("active"));
        tabs[1].classList.add("active"); // Real Life tab index = 1
        contents.forEach(c => c.classList.remove("active"));
        contents[1].classList.add("active");

        // Move capsule highlight
        const wrapperWidth = wrapper.offsetWidth;
        const padding = 4;
        const capsuleWidth = wrapperWidth / totalTabs - 2 * padding;
        highlight.style.width = `${capsuleWidth}px`;
        highlight.style.left = `${1 * (wrapperWidth / totalTabs) + padding}px`;

        // Scroll to the story smoothly with some offset (partial view above/below)
        const storyElement = document.getElementById(storyId);
        if (storyElement) {
            const offset = 100; // adjust how much of the story above you want
            const elementPosition = storyElement.getBoundingClientRect().top + window.scrollY - offset;
            window.scrollTo({
                top: elementPosition,
                behavior: "smooth"
            });
        }
    }
});
