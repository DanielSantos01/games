package alieninvasion;

import java.awt.Graphics2D;
import java.awt.image.BufferStrategy;
import java.io.IOException;
import java.util.ArrayList;

public class RunGame {
    private final Screen screen;
    private final Settings settings;
    private final Ship ship;
    private Graphics2D g;
    private Alien alien;
    private final ArrayList<Alien> fleet;
    
    public RunGame(Screen scr, Settings set, Ship shp){
        screen = scr;
        settings = set;
        ship = shp;
        fleet = new ArrayList();
    }
    
    protected void start() throws IOException{
        while(true) update();
    }
    
    private void update() throws IOException{
        BufferStrategy bs = settings.canvas.getBufferStrategy();
        if(bs == null) {
            settings.canvas.createBufferStrategy(2);
            return;
        }
        g = (Graphics2D) bs.getDrawGraphics();
        
        updateScreen();
        
        g.dispose();
        bs.show();
    }
    
    private void updateScreen() throws IOException{
        settings.clock(30);
        screen.fill(g);
        ship.run(g);
        
        if(settings.createFleet) createFleet();
        drawFleet();
        checkFleetBorder();
    }
    
    private void createFleet() throws IOException{
        for(int x = 0; x <= 7; x++){
            alien = new Alien(settings);
            alien.rect.x = 30 + x*2*alien.rect.width;
            alien.rect.y = 30;
            fleet.add(alien);
        }
        settings.createFleet = false;
    }
    
    private void drawFleet(){
        fleet.stream().forEach((al) -> {
            al.execute(g);
        });
    }
    
    private void checkFleetBorder(){
        for(Alien al : fleet){
            if(al.touch){
                changeFleet();
                break;
            }
        }
    }
    
    private void changeFleet(){
        fleet.stream().forEach((al) -> {
            al.changeDirection();
            al.goDown();
        });
    }
}
