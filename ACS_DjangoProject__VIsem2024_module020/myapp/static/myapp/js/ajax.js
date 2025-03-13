document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.getElementById('search-button');
    const searchInput = document.getElementById('search-input');
    const resultsContainer = document.getElementById('results-container');

    searchButton.addEventListener('click', function() {
        const query = searchInput.value;
        fetch(`/search_student/?q=${query}`)
            .then(response => response.json())
            .then(data => {
                resultsContainer.innerHTML = ''; // Clear previous results
                if (data.results.length > 0) {
                    data.results.forEach(student => {
                        const studentElement = document.createElement('div');
                        studentElement.textContent = student.name;
                        resultsContainer.appendChild(studentElement);
                    });
                } else {
                    resultsContainer.textContent = 'No students found.';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                resultsContainer.textContent = 'An error occurred while fetching data.';
            });
    });
});
