// Get the form and expense list elements
const form = document.getElementById('expense-form');
const expensesList = document.getElementById('expenses-list');

// Initialize the categories array
let categories = ['Food', 'Transportation', 'Entertainment', 'Miscellaneous'];

// Function to render the select category dropdown
function renderCategoryDropdown() {
    const categorySelect = document.getElementById('category');
    categorySelect.innerHTML = '';

    categories.forEach(category => {
        const option = document.createElement('option');
        option.value = category;
        option.textContent = category;
        categorySelect.appendChild(option);
    });
}

// Event listener for the form submit
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the date and category from the form fields
    const date = document.getElementById('date').value;
    const categoryValue = document.getElementById('category').value;

    // Create a new expense object
    const expense = {
        date,
        category: categoryValue
    };

    // Add the expense to the expenses array
    const expenses = JSON.parse(localStorage.getItem('expenses')) || [];
    expenses.push(expense);

    // Update local storage with the new expenses
    localStorage.setItem('expenses', JSON.stringify(expenses));

    // Render the updated list of expenses
    renderExpensesList();

    // Show the view all expenses button
    document.getElementById('view-all-expenses-btn').style.display = 'block';
});

// Function to render the expenses list
function renderExpensesList() {
    const expenseItems = document.querySelectorAll('.expense-item');

    // Clear any existing expenses from the list
    while (expenseItems.length > 0) {
        expenseItems[0].parentNode.removeChild(expenseItems[0]);
    }

    // Get the expenses array from local storage
    const expenses = JSON.parse(localStorage.getItem('expenses')) || [];

    expenses.forEach((expense, index) => {
        const expenseItem = document.createElement('li');
        expenseItem.className = 'expense-item';

        // Render the expense date and category
        const expenseDate = document.createElement('span');
        expenseDate.textContent = `Date: ${expense.date}`;
        expenseItem.appendChild(expenseDate);

        const expenseCategory = document.createElement('span');
        expenseCategory.className = 'expense-type';
        expenseCategory.textContent = expense.category;
        expenseItem.appendChild(expenseCategory);

        expensesList.appendChild(expenseItem);
    });

    // Get all expenses
    const allExpenses = JSON.parse(localStorage.getItem('expenses')) || [];

    // Render the list of all expenses
    renderAllExpenses(allExpenses);
}

// Function to render the list of all expenses
function renderAllExpenses(expenses) {
    const allExpensesList = document.getElementById('all-expenses-list');

    // Clear any existing expenses from the list
    while (allExpensesList.children.length > 0) {
        allExpensesList.removeChild(allExpensesList.firstChild);
    }

    expenses.forEach((expense, index) => {
        const expenseItem = document.createElement('li');
        expenseItem.className = 'expense-item';

        // Render the expense date and category
        const expenseDate = document.createElement('span');
        expenseDate.textContent = `Date: ${expense.date}`;
        expenseItem.appendChild(expenseDate);

        const expenseCategory = document.createElement('span');
        expenseCategory.className = 'expense-type';
        expenseCategory.textContent = expense.category;
        expenseItem.appendChild(expenseCategory);

        allExpensesList.appendChild(expenseItem);
    });
}

// Function to render the select category dropdown
function renderCategoryDropdown() {
    const categorySelect = document.getElementById('category');
    categorySelect.innerHTML = '';

    categories.forEach(category => {
        const option = document.createElement('option');
        option.value = category;
        option.textContent = category;
        categorySelect.appendChild(option);
    });
}

// Initialize the category dropdown
renderCategoryDropdown();

// Render the initial list of expenses
renderExpensesList();

// Show the view all expenses button
document.getElementById('view-all-expenses-btn').addEventListener('click', () => {
    document.getElementById('all-expenses-modal').style.display = 'block';
});

// Close the modal when clicked outside
document.addEventListener('click', (e) => {
    if (e.target !== document.getElementById('all-expenses-modal')) {
        document.getElementById('all-expenses-modal').style.display = 'none';
    }
});