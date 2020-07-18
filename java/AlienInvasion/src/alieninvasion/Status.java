package alieninvasion;

import java.awt.Color;
import java.awt.Graphics2D;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Status {
    protected int level;
    protected int value;
    protected int chancesLeft;
    protected int highscore;
    private String chancesMessage;
    private String scoreMessage;
    private final String path;
    private final BufferedReader reader;
    private BufferedWriter writer;
    
    public Status() throws FileNotFoundException, IOException{
        level = 1;
        value = 0;
        chancesLeft = 3;
        path = "/home/daniel/Documentos/Programming/Python/Repositórios/Games/java/AlienInvasion/src/score/highscore.txt";
        reader = new BufferedReader(new FileReader(path));
        highscore = Integer.parseInt(reader.readLine());
        reader.close();
    }
    
    protected void draw(Graphics2D g){
        g.setColor(Color.black);
        chancesMessage = chancesLeft + " Chances left";
        g.drawString(chancesMessage, 10, 20);
        scoreMessage = "Level: " + level + " - Score: " + value + " - Highscore: " + highscore;
        g.drawString(scoreMessage, 750, 20);
    }
    
    protected void updateHighscore() throws IOException{
        highscore = value;
        writer = new BufferedWriter(new FileWriter(path));
        writer.write(Integer.toString(highscore));
        writer.close();
    }
}
