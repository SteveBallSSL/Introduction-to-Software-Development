<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script>
        function OK_Clicked(){
            alert('Has been clicked');
        }
    </script>
</head>
<body>
    <h1>Test2</h1>

    <?php
        for ($i=0; $i < 10 ; $i++) { 
            echo $i;
        } 
    ?>
</body>
</html>