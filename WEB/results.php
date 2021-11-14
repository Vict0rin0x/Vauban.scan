<?php


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Vauban Scan</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/js/bootstrap.bundle.min.js"></script>
    <script type="text/javascript" src="/eel.js"></script>
    <script type="text/javascript" src="main.js"></script>
</head>
<body onLoad="fetchCreate()">
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Vauban Scan</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">

        </div>
    </div>
</nav>
<div>
    <table class="table p-3 rounded shadow-lg">
        <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">IP</th>
            <th scope="col">MAC</th>
            <th scope="col">Opened Ports</th>
            <th scope="col">Closed | Unanswered Ports</th>
            <th scope="col">Filtered Ports</th>
            <th scope="col">Possible services running (to be done...)</th>

        </tr>
        </thead>
        <tbody id="tableJS">
        <!--Create tr by js-->
        </tbody>

    </table>
</div>
</body>
</html>