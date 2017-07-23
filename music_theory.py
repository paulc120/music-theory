#################### Major Scales ####################

major_scales = {

    "C":"C, D, E, F, G, A, B, C",
    "C#/Db":"C#, D#, E#, F#, G#, A#, B#, C#",

    "D":"D, E, F#, G, A, B, C#, D",

    "D#/Eb":"Eb, F, G, Ab, Bb, C, D, Eb",
    "E":"E, F#, G#, A, B, C#, D#",

    "F":"F, G, A, Bb, C, D, E, F",
    "F#/Gb":"F#, G#, A#, B, C#, D#, E#, F#",

    "G":"G, A, B, C, D, E, F#, G",

    "G#/Ab":"Ab, Bb, C, Db, Eb, F, G, Ab",
    "A":"A, B, C#, D, E, F#, G#, A",

    "A#/Bb":"Bb, C, D, Eb, F, G, A, Bb",
    "B":"B, C#, D#, E, F#, G#, A#, B"

}



#################### Minor Scales ####################


natural_minor_scales = {

    "C":"C, D, Eb, F, G, Ab, Bb, C",
    "C#/Db":"C#, D#, E, F#, G#, A, B, C#",

    "D":"D, E, F, G, A, Bb, C, D",

    "D#/Eb":"Eb, F, Gb, Ab, Bb, Cb, Db, Eb",
    "E":"E, F#, G, A, B, C, D, E",

    "F":"F, G, Ab, Bb, C, Db, Eb, F",
    "F#/Gb":"F#, G#, A, B, C#, D, E, F#",

    "G":"G, A, Bb, C, D, Eb, F, G",

    "G#/Ab":"Ab, Bb, Cb, Db, Eb, Fb, Gb, Ab",
    "A":"A, B, C, D, E, F, G, A",

    "A#/Bb":"Bb, C, Db, Eb, F, Gb, Ab, Bb",
    "B":"B, C#, D, E, F#, G, A, B"

}

harmonic_minor_scales = {

    "C":"C, D, Eb, F, G, Ab, B, C",
    "C#/Db":"C#, D#, E, F#, G#, A, B#, C#",

    "D":"D, E, F, G, A, Bb, C#, D",

    "D#/Eb":"Eb, F, Gb, Ab, Bb, Cb, D, Eb",
    "E":"E, F#, G, A, B, C, D#, E",

    "F":"F, G, Ab, Bb, C, Db, E, F",
    "F#/Gb":"F#, G#, A, B, C#, D, E#, F#",

    "G":"G, A, Bb, C, D, Eb, F#, G",

    "G#/Ab":"Ab, Bb, Cb, Db, Eb, Fb, G, Ab",
    "A":"A, B, C, D, E, F, G#, A",

    "A#/Bb":"Bb, C, Db, Eb, F, Gb, A, Bb",
    "B":"B, C#, D, E, F#, G, A#, B"

}


melodic_minor_scales = {

    "C Ascend":"Ascending: C, D, Eb, F, G, A, B, C",
    "C Descend":"Descending: C, Bb, Ab, G, F, Eb, D, C",

    "C#/Db Ascend":"Ascending: C#, D#, E, F#, G#, A#, B#, C#",
    "C#/Db Descend":"Descending: C#, B, A, G#, F#, E, D#, C#",

    "D Ascend":"Ascending: D, E, F, G, A, B, C#, D",
    "D Descend":"Descending: D, C, Bb, A, G, F, E, D",

    "D#/Eb Ascend":"Ascending: Eb, F, Gb, Ab, Bb, C, D, Eb",
    "D#/Eb Descend":"Descending: Eb, Db, Cb, Bb, Ab, Gb, F, Eb",

    "E Ascend":"Ascending: E, F#, G, A, B, C#, D#, E",
    "E Descend":"Descending: E, D, C, B, A, G, F#, E",

    "F Ascend":"Ascending: F, G, Ab, Bb, C, D, E, F",
    "F Descend":"Descending: F, Eb, Db, C, Bb, Ab, G, F",


    "F#/Gb Ascend":"Ascending: F#, G#, A, B, C#, D#, E#, F#",
    "F#/Gb Descend":"Descending: F#, E, D, C#, B, A, G#, F#",

    "G Ascend":"Ascending: G, A, Bb, C, D, E, F#, G",
    "G Descend":"Descending: G, F, Eb, D, C, Bb, A, G",

    "G#/Ab Ascend":"Ascending: Ab, Bb, Cb, Db, Eb, F, G, Ab",
    "G#/Ab Descend":"Descending: Ab, Gb, Fb, Eb, Db, Cb, Bb, Ab",

    "A Ascend":"Ascending: A, B, C, D, E, F#, G#, A",
    "A Descend":"Descending: A, G, F, E, D, C, B, A",

    "A#/Bb Ascend":"Ascending: Bb, C, Db, Eb, F, G, A, Bb",
    "A#/Bb Descend":"Descending: Bb, Ab, Gb, F, Eb, Db, C, Bb",


    "B Ascend":"Ascending: B, C#, D, E, F#, G#, A#, B",
    "B Descend":"Descending: B, A, G, F#, E, D, C#, B"

}



#################### Root-Position Triads ####################

root_triads = {

    "C Major Triad":"C E G",
    "C Minor Triad":"C Eb G",
    "C Augmented Triad":"C E# G#",
    "C Diminished Triad":"C Eb Gb",

    "C# Major Triad":"C# E# G#",
    "C# Minor Triad":"C# E G#",
    "C# Augmented Triad":"C# E# Gx",
    "C# Diminished Triad":"C# E G",

    "D Major Triad":"D F# A",
    "D Minor Triad":"D F A",
    "D Augmented Triad":"D F# A#",
    "D Diminished Triad":"D F Ab",

    "Eb Major Triad":"Eb G Bb",
    "Eb Minor Triad":"Eb Gb Bb",
    "Eb Augmented Triad":"Eb G B",
    "Eb Diminished Triad":"Eb Gb Bbb",

    "E Major Triad":"E G# B",
    "E Minor Triad":"E G B",
    "E Augmented Triad":"E G# B#",
    "E Diminished Triad":"E G Bb",

    "F Major Triad":"F A C",
    "F Minor Triad":"F Ab C",
    "F Augmented Triad":"F A C#",
    "F Diminished Triad":"F Ab Cb",

    "F# Major Triad":"F# A# C#",
    "F# Minor Triad":"F# A C#",
    "F# Augmented Triad":"F# A# Cx",
    "F# Diminished Triad":"F# A C",

    "G Major Triad":"G B D",
    "G Minor Triad":"G Bb D",
    "G Augmented Triad":"G B D#",
    "G Diminished Triad":"G Bb Db",

    "Ab Major Triad":"Ab C Eb",
    "Ab Minor Triad":"Ab Cb Eb",
    "Ab Augmented Triad":"Ab C E",
    "Ab Diminished Triad":"Ab Cb Ebb",

    "A Major Triad":"A C# E",
    "A Minor Triad":"A C E",
    "A Augmented Triad":"A C# E#",
    "A Diminished Triad":"A C Eb",

    "Bb Major Triad":"Bb D F",
    "Bb Minor Triad":"Bb Db F",
    "Bb Augmented Triad":"Bb D F#",
    "Bb Diminished Triad":"Bb Db Fb",

    "B Major Triad":"B D# F#",
    "B Minor Triad":"B D F#",
    "B Augmented Triad":"B D Fx",
    "B Diminished Triad":"B D F"

}
#################### Root-Position 7th Chords ####################
root_7th = {

    "C Major Seventh":"C E G B",
    "C Minor Seventh":"C Eb G Bb",
    "C Half-Diminished Seventh":"C Eb Gb Bb",
    "C Diminished Seventh":"C Eb Gb Bbb",

    "C# Major Seventh":"C# E# G# B#",
    "C# Minor Seventh":"C# E G# B",
    "C# Half-Diminished Seventh":"C# E G B",
    "C# Diminished Seventh":"C# E G Bb",

    "D Major Seventh":"D F# A C#",
    "D Minor Seventh":"D F A C",
    "D Half-Diminished Seventh":"D F Ab C",
    "D Diminished Seventh":"D F Ab Cb",

    "Eb Major Seventh":"Eb G Bb D",
    "Eb Minor Seventh":"Eb Gb Bb Db",
    "Eb Half-Diminished Seventh":"Eb Gb Bbb Db",
    "Eb Diminished Seventh":"Eb Gb Bbb Dbb",

    "E Major Seventh":"E G# B D#",
    "E Minor Seventh":"E G B D",
    "E Half-Diminished Seventh":"E G Bb D",
    "E Diminished Seventh":"E G Bb Db",

    "F Major Seventh":"F A C E",
    "F Minor Seventh":"F Ab C Eb",
    "F Half-Diminished Seventh":"F Ab Cb Eb",
    "F Diminished Seventh":"F Ab Cb Ebb",

    "F# Major Seventh":"F# A# C# E#",
    "F# Minor Seventh":"F# A C# E",
    "F# Half-Diminished Seventh":"F# A C E",
    "F# Diminished Seventh":"F# A C Eb",

    "G Major Seventh":"G B D F#",
    "G Minor Seventh":"G Bb D F",
    "G Half-Diminished Seventh":"G Bb Db F",
    "G Diminished Seventh":"G Bb Db Fb",

    "Ab Major Seventh":"Ab C Eb G",
    "Ab Minor Seventh":"Ab Cb Eb Gb",
    "Ab Half-Diminished Seventh":"Ab Cb Ebb Gb",
    "Ab Diminished Seventh":"Ab Cb Ebb Gbb",

    "A Major Seventh":"A C# E G#",
    "A Minor Seventh":"A C E G",
    "A Half-Diminished Seventh":"A C Eb G",
    "A Diminished Seventh":"A C Eb Gb",

    "Bb Major Seventh":"Bb D F A",
    "Bb Minor Seventh":"Bb Db F Ab",
    "Bb Half-Diminished Seventh":"Bb Db Fb Ab",
    "Bb Diminished Seventh":"Bb Db Fb Abb",

    "B Major Seventh":"B D# F# A#",
    "B Minor Seventh":"B D F# A",
    "B Half-Diminished Seventh":"B D F A",
    "B Diminished Seventh":"B D F Ab"

}



#################### Get Major Scales ####################


def get_major_scale():
    print("\nWhat scale would you like? Enter letter and scale")
    print("For example: C Major")
    print("For scales with sharps or flats, use # and b, respectively")

    major_answer = input(">")
    if major_answer.lower() == "c major":
        print("\nThe C Major scale has no sharps or flats. The scale is as follows: ")
        print(major_scales["C"])

    elif major_answer.lower() == "c# major":
        print("\nThe C# Major scale has 7 sharps. The scale is as follows: ")
        print(major_scales["C#/Db"])

    elif major_answer.lower() == "d major":
        print("\nThe D Major scale has 2 sharps. The scale is as follows: ")
        print(major_scales["D"])

    elif major_answer.lower() == "eb major":
        print("\nThe Eb Major scale has 3 flats. The scale is as follows: ")
        print(major_scales["D#/Eb"])

    elif major_answer.lower() == "e major":
        print("\nThe E Major scale has 4 sharps. The scale is as follows: ")
        print(major_scales["E"])

    elif major_answer.lower() == "f major":
        print("\nThe F major scale has 1 flat. The scale is as follows: ")
        print(major_scales["F"])

    elif major_answer.lower() == "f# major":
        print("\nThe F# Major scale has 6 sharps. The scale is as follows: ")
        print(major_scales["F#/Gb"])

    elif major_answer.lower() == "g major":
        print("\nThe E Major scale has 1 sharp. The scale is as follows: ")
        print(major_scales["G"])

    elif major_answer.lower() == "ab major":
        print("\nThe Ab Major scale has 4 flats. The scale is as follows: ")
        print(major_scales["E"])

    elif major_answer.lower() == "a major":
        print("\nThe A Major scale has 3 sharps. The scale is as follows: ")
        print(major_scales["A"])

    elif major_answer.lower() == "bb major":
        print("\nThe Bb Major scale has 2 flats. The scale is as follows: ")
        print(major_scales["Bb"])

    elif major_answer.lower() == "b major":
        print("\nThe B Major scale has 5 sharps. The scale is as follows: ")
        print(major_scales["B"])




#################### Get Minor Scales ####################


def get_minor_type():
    print("\nWhich minor (natural, melodic, or harmonic) scale would you like?")
    print('For example: "natural"')

    minor_answer = input("> ")



    #################### Natural Minor Scale ####################

    def natural_minor_scale():
        print("\nWhat scale would you like? Enter letter and scale")
        print("For example: c natural minor")
        print("For scales with sharps or flats, use # and b, respectively")

        minor_answer1 = input("\nEnter scale (for example, C natural minor): ")

        if minor_answer1 == "c natural minor":
            print("\nThe c natural minor scale has 3 flats. The scale is as follows: ")
            print(natural_minor_scales["C"])

        elif minor_answer1 == "c# natural minor":
            print("\nThe c# natural minor scale has 4 sharps. The scale is as follows: ")
            print(natural_minor_scales["C#"])

        elif minor_answer1 == "d natural minor":
            print("\nThe d natural minor scale has 1 flat. The scale is as follows: ")
            print(natural_minor_scales["D"])

        elif minor_answer1.lower() == "eb natural minor":
            print("\nThe eb natural minor has 6 flats. The scale is as follows: ")
            print(natural_minor_scales["D#/Eb"])

        elif minor_answer1.lower() == "e natural minor":
            print("\nThe e natural minor has 1 sharp. The scale is as follows: ")
            print(natural_minor_scales["E"])

        elif minor_answer1.lower() == "f natural minor":
            print("\nThe f natural minor has 4 flats. The scale is as follows: ")
            print(natural_minor_scales["F"])

        elif minor_answer1.lower() == "f# natural minor":
            print("\nThe f# natural minor has 3 sharps. The scale is as follows: ")
            print(natural_minor_scales["F#/Gb"])

        elif minor_answer1.lower() == "g natural minor":
            print("\nThe e natural minor has 2 flats. The scale is as follows: ")
            print(natural_minor_scales["G"])

        elif minor_answer1.lower() == "ab natural minor":
            print("\nThe ab natural minor has 7 flats. The scale is as follows: ")
            print(natural_minor_scales["G#/Ab"])

        elif minor_answer1.lower() == "a natural minor":
            print("\nThe a natural minor has no sharps or flats. The scale is as follows: ")
            print(natural_minor__scales["A"])

        elif minor_answer1.lower() == "bb natural minor":
            print("\nThe bb natural minor has 5 flats. The scale is as follows: ")
            print(natural_minor_r_scales["Bb"])

        elif minor_answer1.lower() == "b natural minor":
            print("\nThe b natural minor has 2 sharps. The scale is as follows: ")
            print(natural_minor__scales["B"])






    #################### Harmonic Minor Scale ####################

    def harmonic_minor_scale():
        print("\nFor scales with sharps or flats, use # and b, respectively")

        minor_answer2 = input("Enter scale (for example, C harmonic minor): ")

        if minor_answer2 == "c harmonic minor":
            print("\nThe c harmonic minor scale has 2 flats. The scale is as follows: ")
            print(harmonic_minor_scales["C"])

        elif minor_answer2 == "c# harmonic minor":
            print("\nThe c# harmonic minor scale has 5 sharps. The scale is as follows: ")
            print(harmonic_minor_scales["C#"])

        elif minor_answer2 == "d harmonic minor":
            print("\nThe d harmonic minor scale has 1 flat and 1 sharp. The scale is as follows: ")
            print(harmonic_minor_scales["D"])

        elif minor_answer2.lower() == "eb harmonic minor":
            print("\nThe eb harmonic minor has 5 flats. The scale is as follows: ")
            print(harmonic_minor_scales["D#/Eb"])

        elif minor_answer2.lower() == "e harmonic minor":
            print("\nThe e harmonic minor has 2 sharps. The scale is as follows: ")
            print(harmonic_minor_scales["E"])

        elif minor_answer2.lower() == "f harmonic minor":
            print("\nThe f harmonic minor has 3 flats. The scale is as follows: ")
            print(harmonic_minor_scales["F"])

        elif minor_answer2.lower() == "f# harmonic minor":
            print("\nThe f# harmonic minor has 4 sharps. The scale is as follows: ")
            print(harmonic_minor_scales["F#/Gb"])

        elif minor_answer2.lower() == "g harmonic minor":
            print("\nThe e harmonic minor has 2 flats and 1 sharp. The scale is as follows: ")
            print(harmonic_minor_scales["G"])

        elif minor_answer2.lower() == "ab harmonic minor":
            print("\nThe ab harmonic minor has 6 flats. The scale is as follows: ")
            print(harmonic_minor_scales["G#/Ab"])

        elif minor_answer2.lower() == "a harmonic minor":
            print("\nThe a harmonic minor has 1 sharp. The scale is as follows: ")
            print(harmonic_minor_scales["A"])

        elif minor_answer2.lower() == "bb harmonic minor":
            print("\nThe bb harmonic minor has 4 flats. The scale is as follows: ")
            print(harmonic_minor_scales["Bb"])

        elif minor_answer2.lower() == "b harmonic minor":
            print("\nThe b harmonic minor has 3 sharps. The scale is as follows: ")
            print(harmonic_minor_scales["B"])


    #################### Melodic Minor Scale  ####################

    def melodic_minor_scale():
        print("\nWhat scale would you like? Enter letter and scale")
        print("For example: c natural minor")
        print("For scales with sharps or flats, use # and b, respectively")

        minor_answer3 = input("\nEnter scale (for example, C melodic minor): ")

        if minor_answer3.lower() == "c melodic minor":
            print("\nThe C melodic minor scale is as follows: \n")
            print(melodic_minor_scales["C Ascend"])
            print(melodic_minor_scales["C Descend"])

        elif minor_answer3.lower() == "c# melodic minor":
            print("\nThe C# melodic minor scale is as follows: \n")
            print(melodic_minor_scales["C#/Db Ascend"])
            print(melodic_minor_scales["C#/Db Descend"])

        elif minor_answer3.lower() == "d melodic minor":
            print("\nThe D melodic minor scale is as follows: \n")
            print(melodic_minor_scales["D Ascend"])
            print(melodic_minor_scales["D Descend"])

        elif minor_answer3.lower() == "eb melodic minor":
            print("\nThe Eb melodic minor scale is as follows: \n")
            print(melodic_minor_scales["D#/Eb Ascend"])
            print(melodic_minor_scales["D#/Eb Descend"])

        elif minor_answer3.lower() == "e melodic minor":
            print("\nThe E melodic minor scale is as follows: \n")
            print(melodic_minor_scales["E Ascend"])
            print(melodic_minor_scales["E Descend"])

        elif minor_answer3.lower() == "f melodic minor":
            print("\nThe F melodic minor scale is as follows: \n")
            print(melodic_minor_scales["F Ascend"])
            print(melodic_minor_scales["F Descend"])

        elif minor_answer3.lower() == "f# melodic minor":
            print("\nThe F# melodic minor scale is as follows: \n")
            print(melodic_minor_scales["F#/Gb Ascend"])
            print(melodic_minor_scales["F#/Gb Descend"])

        elif minor_answer3.lower() == "g melodic minor":
            print("\nThe G melodic minor scale is as follows: \n")
            print(melodic_minor_scales["G Ascend"])
            print(melodic_minor_scales["G Descend"])

        elif minor_answer3.lower() == "ab melodic minor":
            print("\nThe Ab melodic minor scale is as follows: \n")
            print(melodic_minor_scales["G#/Ab Ascend"])
            print(melodic_minor_scales["G#/Ab Descend"])

        elif minor_answer3.lower() == "a melodic minor":
            print("\nThe A melodic minor scale is as follows: \n")
            print(melodic_minor_scales["A Ascend"])
            print(melodic_minor_scales["A Descend"])

        elif minor_answer3.lower() == "bb melodic minor":
            print("\nThe Bb melodic minor scale is as follows: \n")
            print(melodic_minor_scales["A#/Bb Ascend"])
            print(melodic_minor_scales["A#/Bb Descend"])

        elif minor_answer3.lower() == "b melodic minor":
            print("\nThe B melodic minor scale is as follows: \n")
            print(melodic_minor_scales["B Ascend"])
            print(melodic_minor_scales["B Descend"])

    if minor_answer.lower() == "natural":
        natural_minor_scale()

    elif minor_answer.lower() == "harmonic":
        harmonic_minor_scale()

    elif minor_answer.lower() == "melodic":
        melodic_minor_scale()



#################### Root-Position Triads ####################

def triad_chords():

    three_quality = input("\nWhat chord quality would you like? Enter major, minor, diminished, or augmented: ")


    #################### Major Triads ####################

    if three_quality.lower() == "major":

        major_quality = input("\n\nEnter note name (for example: C or C#): ")
        mm = print("\n\n**The '#' accidental = sharp**\n**The 'b' accidental = flat**\n**The 'x' accidental = double sharp**\n**The 'bb' accidental = double flat**")

        if major_quality.lower() == "c":
            mm
            print("\nThe notes in the C Major triad consists of:")
            print(root_triads["C Major Triad"])

        elif major_quality.lower() == "c#":
            mm
            print("\nThe notes in the C# Major triad consists of:")
            print(root_triads["C# Major Triad"])

        elif major_quality.lower() == "d":
            mm
            print("\nThe notes in the D Major triad consists of:")
            print(root_triads["D Major Triad"])

        elif major_quality.lower() == "eb":
            mm
            print("\nThe notes in the Eb Major triad consists of:")
            print(root_triads["Eb Major Triad"])

        elif major_quality.lower() == "e":
            mm
            print("\nThe notes in the E Major triad consists of:")
            print(root_triads["E Major Triad"])

        elif major_quality.lower() == "f":
            mm
            print("\nThe notes in the F Major triad consists of:")
            print(root_triads["F Major Triad"])

        elif major_quality.lower() == "f#":
            mm
            print("\nThe notes in the F# Major triad consists of:")
            print(root_triads["F# Major Triad"])

        elif major_quality.lower() == "g":
            mm
            print("\nThe notes in the Eb Major triad consists of:")
            print(root_triads["Eb Major Triad"])

        elif major_quality.lower() == "ab":
            mm
            print("\nThe notes in the Ab Major triad consists of:")
            print(root_triads["Ab Major Triad"])

        elif major_quality.lower() == "a":
            mm
            print("\nThe notes in the A Major triad consists of:")
            print(root_triads["A Major Triad"])

        elif major_quality.lower() == "bb":
            mm
            print("\nThe notes in the Bb Major triad consists of:")
            print(root_triads["Bb Major Triad"])

        elif major_quality.lower() == "b":
            mm
            print("\nThe notes in the B Major triad consists of:")
            print(root_triads["B Major Triad"])



    #################### Minor Triads ####################

    elif three_quality.lower() == "minor":

        minor_quality = input("\n\nEnter note name (for example C or C#): ")
        m = print("\n\n**The '#' accidental = sharp**\n**The 'b' accidental = flat**\n**The 'x' accidental = double sharp**\n**The 'bb' accidental = double flat**")

        if minor_quality.lower() == "c":
            m
            print("\nThe notes in the C minor triad consists of:")
            print(root_triads["C Minor Triad"])

        elif minor_quality.lower() == "c#":
            m
            print("\nThe notes in the C# minor triad consists of:")
            print(root_triads["C# Minor Triad"])

        elif minor_quality.lower() == "d":
            m
            print("\nThe notes in the D minor triad consists of:")
            print(root_triads["D Minor Triad"])

        elif minor_quality.lower() == "eb":
            m
            print("\nThe notes in the Eb minor triad consists of:")
            print(root_triads["Eb Minor Triad"])

        elif minor_quality.lower() == "e":
            m
            print("\nThe notes in the E minor triad consists of:")
            print(root_triads["E Minor Triad"])

        elif minor_quality.lower() == "f":
            m
            print("\nThe notes in the F minor triad consists of:")
            print(root_triads["F Minor Triad"])

        elif minor_quality.lower() == "f#":
            m
            print("\nThe notes in the F# minor triad consists of:")
            print(root_triads["F# Minor Triad"])

        elif minor_quality.lower() == "g":
            m
            print("\nThe notes in the G minor triad consists of:")
            print(root_triads["G Minor Triad"])

        elif minor_quality.lower() == "ab":
            m
            print("\nThe notes in the Ab minor triad consists of:")
            print(root_triads["Ab Minor Triad"])

        elif minor_quality.lower() == "a":
            m
            print("\nThe notes in the A minor triad consists of:")
            print(root_triads["A Minor Triad"])

        elif minor_quality.lower() == "Bb":
            m
            print("\nThe notes in the Bb minor triad consists of:")
            print(root_triads["Bb Minor Triad"])

        elif minor_quality.lower() == "b":
            m
            print("\nThe notes in the B minor triad consists of:")
            print(root_triads["B Minor Triad"])



    #################### Augmented Triads ####################

    elif three_quality.lower() == "augmented":

        augmented_quality = input("\n\nEnter note name (for example C or C#): ")
        a = print("\n\n**The '#' accidental = sharp**\n**The 'b' accidental = flat**\n**The 'x' accidental = double sharp**\n**The 'bb' accidental = double flat**")

        if augmented_quality.lower() == "c":
            a
            print("\nThe notes in the C Augmented triad consists of:")
            print(root_triads["C Augmented Triad"])

        elif augmented_quality.lower() == "c#":
            a
            print("\nThe notes in the C# Augmented triad consists of:")
            print(root_triads["C# Augmented Triad"])

        elif augmented_quality.lower() == "d":
            a
            print("\nThe notes in the D Augmented triad consists of:")
            print(root_triads["D Augmented Triad"])

        elif augmented_quality.lower() == "eb":
            a
            print("\nThe notes in the Eb Augmented triad consists of:")
            print(root_triads["Eb Augmented Triad"])

        elif augmented_quality.lower() == "e":
            a
            print("\nThe notes in the E Augmented triad consists of:")
            print(root_triads["E Augmented Triad"])

        elif augmented_quality.lower() == "f":
            a
            print("\nThe notes in the F Augmented triad consists of:")
            print(root_triads["F Augmented Triad"])

        elif augmented_quality.lower() == "f#":
            a
            print("\nThe notes in the F# Augmented triad consists of:")
            print(root_triads["F# Augmented Triad"])

        elif augmented_quality.lower() == "g":
            a
            print("\nThe notes in the G Augmented triad consists of:")
            print(root_triads["G Augmented Triad"])

        elif augmented_quality.lower() == "ab":
            a
            print("\nThe notes in the Ab Augmented triad consists of:")
            print(root_triads["Ab Augmented Triad"])

        elif augmented_quality.lower() == "a":
            a
            print("\nThe notes in the A Augmented triad consists of:")
            print(root_triads["A Augmented Triad"])

        elif augmented_quality == "Bb":
            a
            print("\nThe notes in the Bb Augmented triad consists of:")
            print(root_triads["Bb Augmented Triad"])

        elif augmented_quality.lower() == "b":
            a
            print("\nThe notes in the B Augmented triad consists of:")
            print(root_triads["B Augmented Triad"])


    #################### Diminished Triads ####################

    elif three_quality.lower() == "diminished":

        diminished_quality = input("\n\nEnter note name (for example C or C#): ")
        d = print("\n\n**The '#' accidental = sharp**\n**The 'b' accidental = flat**\n**The 'x' accidental = double sharp**\n**The 'bb' accidental = double flat**")

        if diminished_quality.lower() == "c":
            d
            print("\nThe notes in the C diminished triad consists of:")
            print(root_triads["C Diminished Triad"])

        elif diminished_quality.lower() == "c#":
            d
            print("\nThe notes in the C# diminished triad consists of:")
            print(root_triads["C# Diminished Triad"])

        elif diminished_quality.lower() == "d":
            d
            print("\nThe notes in the D diminished triad consists of:")
            print(root_triads["D Diminished Triad"])

        elif diminished_quality.lower() == "eb":
            d
            print("\nThe notes in the Eb diminished triad consists of:")
            print(root_triads["Eb Diminished Triad"])

        elif diminished_quality.lower() == "e":
            d
            print("\nThe notes in the E diminished triad consists of:")
            print(root_triads["E Diminished Triad"])

        elif diminished_quality.lower() == "f":
            d
            print("\nThe notes in the F diminished triad consists of:")
            print(root_triads["F Diminished Triad"])

        elif diminished_quality.lower() == "f#":
            d
            print("\nThe notes in the F# diminished triad consists of:")
            print(root_triads["F# Diminished Triad"])

        elif diminished_quality.lower() == "g":
            d
            print("\nThe notes in the G diminished triad consists of:")
            print(root_triads["G Diminished Triad"])

        elif diminished_quality.lower() == "ab":
            d
            print("\nThe notes in the Ab diminished triad consists of:")
            print(root_triads["Ab Diminished Triad"])

        elif diminished_quality.lower() == "a":
            d
            print("\nThe notes in the A diminished triad consists of:")
            print(root_triads["A Diminished Triad"])

        elif diminished_quality == "Bb":
            d
            print("\nThe notes in the Bb diminished triad consists of:")
            print(root_triads["Bb Diminished Triad"])

        elif diminished_quality.lower() == "b":
            d
            print("\nThe notes in the B diminished triad consists of:")
            print(root_triads["B Diminished Triad"])




#################### Root Seventh Chords ####################

def seventh_chords():

    four_quality = input('\nWhat chord quality would you like? Enter "major", "minor", "half-diminished", or "fully-diminished": ')



    #################### Major Seventh Chords ####################

    if four_quality.lower() == "major":
        major7_quality = input("\n\nEnter note name (for example C or C#): ")
        mm7 = print("\n\n**The '#' accidental = sharp**\n**The 'b' accidental = flat**\n**The 'x' accidental = double sharp**\n**The 'bb' accidental = double flat**")

        if major7_quality.lower() == "c":
            mm7
            print("\nThe notes in the C Major Seventh chord consists of:")
            print(root_7th["C Major Seventh"])

        elif major7_quality.lower() == "c#":
            mm7
            print("\nThe notes in the C# Major Seventh chord consists of:")
            print(root_7th["C# Major Seventh"])

        elif major7_quality.lower() == "d":
            mm7
            print("\nThe notes in the D Major Seventh chord consists of:")
            print(root_7th["D Major Seventh"])

        elif major7_quality.lower() == "eb":
            mm7
            print("\nThe notes in the Eb Major Seventh chord consists of:")
            print(root_7th["Eb Major Seventh"])

        elif major7_quality.lower() == "e":
            mm7
            print("\nThe notes in the E Major Seventh chord consists of:")
            print(root_7th["E Major Seventh"])

        elif major7_quality.lower() == "f":
            mm7
            print("\nThe notes in the F Major Seventh chord consists of:")
            print(root_7th["F Major Seventh"])

        elif major7_quality.lower() == "f#":
            mm7
            print("\nThe notes in the F# Major Seventh chord consists of:")
            print(root_7th["F# Major Seventh"])

        elif major7_quality.lower() == "g":
            mm7
            print("\nThe notes in the Eb Major Seventh chord consists of:")
            print(root_7th["Eb Major Seventh"])

        elif major7_quality.lower() == "ab":
            mm7
            print("\nThe notes in the Ab Major Seventh chord consists of:")
            print(root_7th["Ab Major Seventh"])

        elif major7_quality.lower() == "a":
            mm7
            print("\nThe notes in the A Major Seventh chord consists of:")
            print(root_7th["A Major Seventh"])

        elif major7_quality.lower() == "bb":
            mm7
            print("\nThe notes in the Bb Major Seventh chord consists of:")
            print(root_7th["Bb Major Seventh"])

        elif major7_quality.lower() == "b":
            mm7
            print("\nThe notes in the B Major Seventh chord consists of:")
            print(root_7th["B Major Seventh"])



    #################### Minor Seventh Chords ####################

    elif four_quality.lower() == "minor":
        minor7_quality = input("\n\nEnter note name (for example C or C#): ")
        m7 = print("\n\n**The '#' accidental = sharp**\n**The 'b' accidental = flat**\n**The 'x' accidental = double sharp**\n**The 'bb' accidental = double flat**")

        if minor7_quality.lower() == "c":
            m7
            print("\nThe notes in the C Minor Seventh chord consists of:")
            print(root_7th["C Minor Seventh"])

        elif minor7_quality.lower() == "c#":
            m7
            print("\nThe notes in the C# Minor Seventh chord consists of:")
            print(root_7th["C# Minor Seventh"])

        elif minor7_quality.lower() == "d":
            m7
            print("\nThe notes in the D Minor Seventh chord consists of:")
            print(root_7th["D Minor Seventh"])

        elif minor7_quality.lower() == "eb":
            m7
            print("\nThe notes in the Eb Minor Seventh chord consists of:")
            print(root_7th["Eb Minor Seventh"])

        elif minor7_quality.lower() == "e":
            m7
            print("\nThe notes in the E Minor Seventh chord consists of:")
            print(root_7th["E Minor Seventh"])

        elif minor7_quality.lower() == "f":
            m7
            print("\nThe notes in the F Minor Seventh chord consists of:")
            print(root_7th["F Minor Seventh"])

        elif minor7_quality.lower() == "f#":
            m7
            print("\nThe notes in the F# Minor Seventh chord consists of:")
            print(root_7th["F# Minor Seventh"])

        elif minor7_quality.lower() == "g":
            m7
            print("\nThe notes in the Eb Minor Seventh chord consists of:")
            print(root_7th["Eb Minor Seventh"])

        elif minor7_quality.lower() == "ab":
            m7
            print("\nThe notes in the Ab Minor Seventh chord consists of:")
            print(root_7th["Ab Minor Seventh"])

        elif minor7_quality.lower() == "a":
            m7
            print("\nThe notes in the A Minor Seventh chord consists of:")
            print(root_7th["A Minor Seventh"])

        elif minor7_quality.lower() == "bb":
            m7
            print("\nThe notes in the Bb Minor Seventh chord consists of:")
            print(root_7th["Bb Minor Seventh"])

        elif minor7_quality.lower() == "b":
            m7
            print("\nThe notes in the B Minor Seventh chord consists of:")
            print(root_7th["B Minor Seventh"])


    #################### Half-Diminished Seventh Chords ####################

    elif four_quality.lower() == "half-diminished":

        hd7_quality = input("\n\nEnter note name (for example C or C#): ")
        hd7 = print("\n\n**The '#' accidental = sharp**\n**The 'b' accidental = flat**\n**The 'x' accidental = double sharp**\n**The 'bb' accidental = double flat**")

        if hd7_quality.lower() == "c":
            hd7
            print("\nThe notes in the C Half-Diminished Seventh chord consists of:")
            print(root_7th["C Half-Diminished Seventh"])

        elif hd7_quality.lower() == "c#":
            hd7
            print("\nThe notes in the C# Half-Diminished Seventh chord consists of:")
            print(root_7th["C# Half-Diminished Seventh"])

        elif hd7_quality.lower() == "d":
            hd7
            print("\nThe notes in the D Half-Diminished Seventh chord consists of:")
            print(root_7th["D Half-Diminished"])

        elif hd7_quality.lower() == "eb":
            hd7
            print("\nThe notes in the Eb Half-Diminished Seventh chord consists of:")
            print(root_7th["Eb Half-Diminished Seventh"])

        elif hd7_quality.lower() == "e":
            hd7
            print("\nThe notes in the E Half-Diminished Seventh chord consists of:")
            print(root_7th["E Half-Diminished Seventh"])

        elif hd7_quality.lower() == "f":
            hd7
            print("\nThe notes in the F Half-Diminished Seventh chord consists of:")
            print(root_7th["F Half-Diminished Seventh"])

        elif hd7_quality.lower() == "f#":
            hd7
            print("\nThe notes in the F# Half-Diminished Seventh chord consists of:")
            print(root_7th["F# Half-Diminished Seventh"])

        elif hd7_quality.lower() == "g":
            hd7
            print("\nThe notes in the Eb Half-Diminished Seventh chord consists of:")
            print(root_7th["Eb Half-Diminished Seventh"])

        elif hd7_quality.lower() == "ab":
            hd7
            print("\nThe notes in the Ab Half-Diminished Seventh chord consists of:")
            print(root_7th["Ab Half-Diminished Seventh"])

        elif hd7_quality.lower() == "a":
            hd7
            print("\nThe notes in the A Half-Diminished Seventh chord consists of:")
            print(root_7th["A Half-Diminished Seventh"])

        elif hd7_quality.lower() == "bb":
            hd7
            print("\nThe notes in the Bb Half-Diminished Seventh chord consists of:")
            print(root_7th["Bb Half-Diminished Seventh"])

        elif hd7_quality.lower() == "b":
            hd7
            print("\nThe notes in the B Half-Diminished Seventh chord consists of:")
            print(root_7th["B Half-Diminished Seventh"])



    #################### Fully Diminished Seventh Chords ####################

    elif four_quality.lower() == "fully-diminished":
        diminished7_quality = input("\n\nEnter note name (for example C or C#): ")
        d7 = print("\n\n**The '#' accidental = sharp**\n**The 'b' accidental = flat**\n**The 'x' accidental = double sharp**\n**The 'bb' accidental = double flat**")

        if diminished7_quality.lower() == "c":
            d7
            print("\nThe notes in the C Diminished Seventh chord consists of:")
            print(root_7th["C Diminished Seventh"])

        elif diminished7_quality.lower() == "c#":
            d7
            print("\nThe notes in the C# Diminished Seventh chord consists of:")
            print(root_7th["C# Diminished Seventh"])

        elif diminished7_quality.lower() == "d":
            d7
            print("\nThe notes in the D Diminished Seventh chord consists of:")
            print(root_7th["C# Diminished Seventh"])

        elif diminished7_quality.lower() == "eb":
            d7
            print("\nThe notes in the Eb Diminished Seventh chord consists of:")
            print(root_7th["Eb Diminished Seventh"])

        elif diminished7_quality.lower() == "e":
            d7
            print("\nThe notes in the E Diminished Seventh chord consists of:")
            print(root_7th["E Diminished Seventh"])

        elif diminished7_quality.lower() == "f":
            d7
            print("\nThe notes in the F Diminished Seventh chord consists of:")
            print(root_7th["F Diminished Seventh"])

        elif diminished7_quality.lower() == "f#":
            d7
            print("\nThe notes in the F# Diminished Seventh chord consists of:")
            print(root_7th["F# Diminished Seventh"])

        elif diminished7_quality.lower() == "g":
            d7
            print("\nThe notes in the G Diminished Seventh chord consists of:")
            print(root_7th["G Diminished Seventh"])

        elif diminished7_quality.lower() == "ab":
            d7
            print("\nThe notes in the Ab Diminished Seventh chord consists of:")
            print(root_7th["Ab Diminished Seventh"])

        elif diminished7_quality.lower() == "a":
            d7
            print("\nThe notes in the A Diminished Seventh chord consists of:")
            print(root_7th["A Diminished Seventh"])

        elif diminished7_quality.lower() == "bb":
            d7
            print("\nThe notes in the Bb Diminished Seventh chord consists of:")
            print(root_7th["Bb Diminished Seventh"])

        elif diminished7_quality.lower() == "b":
            d7
            print("\nThe notes in the B Diminished Seventh chord consists of:")
            print(root_7th["B Diminished Seventh"])


#################### Start Program ####################

def start():

    main_menu = input('\nWhat would you like to learn? Enter "chords" or "scales": ')


    def scales():

        get_scale_type = input("Enter which scale you would like (major or minor): ")

        if get_scale_type.lower() == "major":
            get_major_scale()

        elif get_scale_type.lower() == "minor":
            get_minor_type()


    def chords():

        get_chord_type = input('Enter "triads" or "seventh chords": ')

        if get_chord_type.lower() == "triads":
            triad_chords()

        elif get_chord_type.lower() == "seventh chords":
            seventh_chords()


    if main_menu.lower() == "scales":
        scales()

    elif main_menu.lower() == "chords":
        chords()


start()


while True: #if user wants more scales
    get_more = input("\nWould you like more? ")

    if get_more == "yes":
        start()

    else:
        break

print("Goodbye\n")
