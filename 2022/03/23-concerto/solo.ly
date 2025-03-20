\version "2.22.2"
\language "deutsch"
\pointAndClickOff
#(ly:set-option 'backend 'svg)

\header { tagline = ##f}

\paper {
     page-breaking = #ly:one-line-auto-height-breaking
}

\score {

    \new Staff <<
        \set Score.barNumberVisibility = #all-bar-numbers-visible
        \set Score.currentBarNumber = #164
        \key d \major
        % \override Staff.TimeSignature.break-visibility = #(#f #f #f)
        \time 3/4

        \new Voice \relative c'' {
            \voiceOne
            s4*3 | s4*3 | s4*2  e4~-> | e8
        }

        \new Voice \relative c'' {
            \stemDown
            \shiftOn

            \bar ""
            r8 <e gis, e>-. <e a, fis>-. <e h gis>-. <e d h>4->~ |
            <e d h>8 <e c a>-. <e c a>-. <e a, fis>-. <e h gis>-. <e gis, e>-. |
            r8 <e a, f>-. <e h gis>-. <e c a>-. 
            \voiceTwo \once \override NoteColumn.force-hshift = #1.0 <e c>4~ | 
            \once \override NoteColumn.force-hshift = #1.0 <e c>8 
            \oneVoice <e d h>-. <e d h>-. <e h gis>-. <e c a>-. <e a, f>-. |
        
        }
    >>

    \layout {
        indent = 0
        ragged-right = ##t

        \context {
            \Staff
            \remove "Time_signature_engraver"
        }
    }
}
