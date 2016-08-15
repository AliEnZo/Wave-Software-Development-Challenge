
<?php
$r  = json_decode(exec('C:\xampp\htdocs\WaveCompany\MainForm.py'), true);

// array of months
$Month_names = array( 1 => "January",
                    2 => "February",
                    3 => "March",
                    4 => "April",
                    5 => "May",
                    6 => "June",
                    7 => "July",
                    8 => "August",
                    9 => "September",
                    10 => "October",
                    11 => "November",
                    12 => "December");

echo"<html> <link rel='stylesheet' type='text/css' href='CSS/style.css'>";

echo "<table border='1'>
<tr>
<th>Month</th>
<th>Total Expenses Amount</th>
</tr>";

for($j = 1; $j<13; $j++)
{
    echo "<tr>";
    echo "<td>" .$j,' - ',  $Month_names[$j] ."</td>";
    echo "<td>" .$r[$j] , " $ " ."</td>";
    echo "</tr>";
}
echo "</table>";

echo"</html>";

?>
