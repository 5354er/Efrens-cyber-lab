<?php
$servername = "localhost";
$username = "testuser";
$password = "password123";
$dbname = "testdb";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if (isset($_GET['cat'])) {
    $cat = $_GET['cat']; // No sanitization (intentionally vulnerable)
    $sql = "SELECT * FROM products WHERE category = '$cat'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo "ID: " . $row["id"]. " - Name: " . $row["name"]. " - Category: " . $row["category"]. "<br>";
        }
    } else {
        echo "0 results";
    }
}

$conn->close();
?>
