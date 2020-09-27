<?php

function product($arr,$n)
{
    if($n == 1)
    {
        echo "0";
        return;
    }
    $i ; $temp = 1;
    $prod = array();
    for($j = 0; $j < $n; $j++)
    {
        $prod[$j] = 1;
    }
    for($i = 0; $i < $n; $i++)
    {
        $prod[$i] = $temp;
        $temp *= $arr[$i];
    }
    $temp = 1;
    for($i = $n-1; $i >= 0; $i--)
    {
        $prod[$i] *= $temp;
        $temp *= $arr[$i];
    }
    for($i = 0; $i < $n; $i++)
    {
        echo $prod[$i], " ";
    }
    return;
}
$arr = array(1,2,3,4,5);
$n = count($arr);
echo " Product Array :- \n";
product($arr,$n);
?>