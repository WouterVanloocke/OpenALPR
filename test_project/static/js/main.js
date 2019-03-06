function diff_minutes( dt1) 
 {
  dt2 = new Date();
  var diff =(dt2.getTime() - dt1.getTime()) / 1000;
  diff /= 60;
  return Math.abs(Math.round(diff));
  
 }
