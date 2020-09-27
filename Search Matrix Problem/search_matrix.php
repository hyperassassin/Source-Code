<?php
function search(&$mat , $n ,$x)
{
    $i = 0;
    $j = $n-1;
    while($i < $n && $j >= 0)
    {
        if($mat[$i][$j] == $x)
        {
            echo "Element Found at :- ".$i.",".$j;
            return 1;
        }
        if($mat[$i][$j] > $x)
        {
            $j--;
        }
        else 
        {
            $i++;
        }
    }
    echo "\n Element Not Found";
    return 0;
}
$mat = array(array(10,20,30,40),
             array(15,25,35,45),
             array(27,29,37,48),
             array(31,33,39,50));
search($mat,4,37);
?>