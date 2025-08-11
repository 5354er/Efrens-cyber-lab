<?php
$cat = $_GET['cat'] ?? '';  // safely get parameter with fallback

$conn = new mysqli('localhost', 'user', 'password', 'database');

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Prepare SQL with a placeholder
$stmt = $conn->prepare("SELECT * FROM products WHERE category = ?");

if ($stmt === false) {
    die("Prepare failed: " . $conn->error);
}

// Bind the parameter as a string ("s")
$stmt->bind_param("s", $cat);

// Execute the prepared statement
$stmt->execute();

// Get the result
$result = $stmt->get_result();

// Fetch and output rows safely
while ($row = $result->fetch_assoc()) {
    echo htmlspecialchars($row['product_name']) . "<br>";
}

$stmt->close();
$conn->close();
?>
