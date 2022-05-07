function vowelsAndConsonants(s) 
{
    vowels = ['a','e','i','o','u'];
    result = "";
    result2 = "";
    for(vowel=0; vowel < s.length; vowel++)
    {   
        // if a,e,i,o or u contained in s print out "variable"
        if (s.includes(s[vowel])) 
        {
            if (vowels.includes(s[vowel]) )
            {
                result += s[vowel];
            }
            else
            {
                result2 += s[vowel];
            }

        }
    }    
    for(y=0; y<result.length; y++)
    {
        console.log(result[y]);
    }
    for(z=0; z<result2.length; z++)
    {
        console.log(result2[z])
    }
}

alphabet = "abcdefghijklmnopqrstuvwxyz";

vowelsAndConsonants(alphabet);