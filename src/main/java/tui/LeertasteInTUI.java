package tui;

import com.googlecode.lanterna.TerminalSize;
import com.googlecode.lanterna.input.KeyStroke;
import com.googlecode.lanterna.input.KeyType;
import com.googlecode.lanterna.terminal.DefaultTerminalFactory;
import com.googlecode.lanterna.terminal.Terminal;
import com.googlecode.lanterna.TextColor;
import com.googlecode.lanterna.graphics.TextGraphics;

public class LeertasteInTUI {
    public static void main(String[] args) {
        try {
            Terminal terminal = new DefaultTerminalFactory().createTerminal();
            terminal.enterPrivateMode();
            terminal.setCursorVisible(false);
            terminal.clearScreen();

            TextGraphics tg = terminal.newTextGraphics(); // <- Das ist neu

            tg.putString(0, 0, "Drück die Leertaste (ESC zum Beenden)");

            boolean running = true;
            while (running) {
                KeyStroke keyStroke = terminal.pollInput();
                if (keyStroke != null) {
                    if (keyStroke.getKeyType() == KeyType.Character && keyStroke.getCharacter() == ' ') {
                        tg.putString(0, 1, "Leertaste erkannt!        ");
                    } else if (keyStroke.getKeyType() == KeyType.Escape) {
                        running = false;
                    }
                }
                Thread.sleep(50);
            }

            terminal.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

