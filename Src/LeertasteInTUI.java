import com.googlecode.lanterna.TerminalSize;
import com.googlecode.lanterna.input.KeyStroke;
import com.googlecode.lanterna.input.KeyType;
import com.googlecode.lanterna.terminal.DefaultTerminalFactory;
import com.googlecode.lanterna.terminal.Terminal;

public class LeertasteInTUI {
    public static void main(String[] args) {
        try {
            Terminal terminal = new DefaultTerminalFactory().createTerminal();
            terminal.enterPrivateMode();
            terminal.setCursorVisible(false);
            terminal.clearScreen();

            terminal.putString(0, 0, "Drück die Leertaste (ESC zum Beenden)", null, null);

            boolean running = true;
            while (running) {
                KeyStroke keyStroke = terminal.pollInput(); // non-blocking
                if (keyStroke != null) {
                    if (keyStroke.getKeyType() == KeyType.Character && keyStroke.getCharacter() == ' ') {
                        terminal.putString(0, 1, "Leertaste erkannt!                   ", null, null);
                    } else if (keyStroke.getKeyType() == KeyType.Escape) {
                        running = false;
                    }
                }

                Thread.sleep(50); // kleine Pause zur CPU-Schonung
            }

            terminal.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

