# WordGen changes v1.02:
-Cleaned up the main() function a bit, and added an easy exit upon start up<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Removed the input() from print_header() as it added extra delay and didn't allow for an immediate exit.<br>
-Did a memory test, no leaks noticed<br>
-Added more comments for future readability<br>
-Removed "❯ It will automatically shut down after 5 seconds..." as it is now pointless<br>
-Future-proofed option 2 by making it read current year for max, instead of being limited to 2025<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Downside is imported date<br>

<br>
<br>
<br>
<br>
<br>

# WordGen changes v1.01: 
-Removed bloat sleeps (14 of them) <br>
-Added randomness to numbers, they were previously set to repeat 123,123,456 and nothing else<br>
-Adjusted code to no longer utilise the time package, making it slightly more lightweight<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Updated option 1 to include random, something that was previously missing entirely. Technically it is possible to generate a file with the same default name, but considering the odds are 1/10000000000 it shouldn’t be an issue.<br>
-Removed many formatting commands due to them not working in every environment and potentially being unfriendly to users with colour impairment.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Technically reduces resources required but by a very minimal amount. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Kept formatting for the title as that should not have negative consequences in other environments.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-ALL line breaks were preserved, and a few were added for extra readability.<br>
-Added some comments throughout code to make it as easy to use for others later on.<br>
-Replaced all clear_screen_with_message() (21) to print() to ensure users can backtrack lines in all environments, allowing users to check filenames and other input later.<br>
-Added utility for count for option<br>
-Option 2-5 are untouched besides removal of formatting.<br>
-Added .strip() to catch any random spaces<br>

Before(left) and after(right): Input:<br>
“the bee movie is a great film”<br>
Words + Numbers (e.g., word123, 123word)<br>
Count 30<br>
![](images/1.01_changes.png)

