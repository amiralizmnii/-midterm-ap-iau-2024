//برنامه ای بنویسید که یک گذرواژه را به عنوان ورودی بگیرد سپس گزارش دهد 
 
Console.WriteLine("In The Name Of God."); 
//مقدار دهی نام کاربری و رمز عبور 
 
 
Console.Write("Enter The Username: "); 
var Username = Console.ReadLine(); 
Console.Write("Enter The Password: "); 
var Password = Console.ReadLine(); 
bool LengthMoreThanEight = Password.Length >= 8; 
bool LengthLessThanTwelve=Password.Length <=12; 
bool containsUppercase = false; 
bool containsLowercase = false; 
bool containsNumbers = false; 
//چاپ کردن شروط نام کاربری و رمز عبور 
Console.WriteLine("Your Username And Password Should Between 8 until 12 Characters."); 
Console.WriteLine("Your Username And Password Should have Uppercase & LowerCase letters & each of (@,#)"); 
//تعیین شرط برای نام کاربری و رمز عبور 
foreach(var c in Password) 
{ 
    if (char.IsUpper(c)) 
    { 
        containsUppercase = true; 
 
    } 
    else if (char.IsLower(c)) 
    { 
        containsLowercase = true; 
    } 
    else if (char.IsNumber(c)) 
    { 
        containsNumbers = true; 
    } 
} 
if (LengthMoreThanEight &&LengthLessThanTwelve && containsUppercase && containsLowercase && containsNumbers) 
{ 
    Console.WriteLine("Your Password Is Strong!"); 
} 
else 
{ 
    Console.WriteLine("Your Password Is Weak!"); 
 
}
