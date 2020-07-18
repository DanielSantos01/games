package alieninvasion;

import java.awt.Graphics2D;
import java.awt.image.BufferStrategy;
import java.io.IOException;
import java.util.ArrayList;

public class RunGame {
    private final Screen screen;
    private final Settings settings;
    private final ArrayList<Alien> fleet;
    private final ArrayList<Bullet> bullets;
    private final Ship ship;
    private final Status status;
    private final Button button;
    private Graphics2D g;
    private Alien alien;
    private Bullet bullet;
    private boolean out;
    private int alienIndex;
    private int bulletIndex;
    
    public RunGame(Screen scr, Settings set, Ship shp) throws IOException{
        screen = scr;
        settings = set;
        ship = shp;
        fleet = new ArrayList();
        bullets = new ArrayList();
        status = new Status();
        button = new Button(settings);
        out = false;
        alienIndex = 0;
        bulletIndex = 0;
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
        status.draw(g);
        ship.run(g);
        
        if(settings.createFleet) createFleet();
        drawFleet();
        checkFleetBorder();
        
        if(settings.shoot && bullets.size() <= 2){
           newShoot();
           settings.shoot = false;
        }
        
        updateBullets();
        
        if(!(bullets.isEmpty())) checkBulletAlien();
        
        if(settings.start) {
            checkAlienShip();
            checkLevel();
        }
        
        if(settings.preStart || settings.gameOver) button.draw(g);
        
    }
    
    //-------------------------------------------------------------------------------------------------------------
    
    private void createFleet() throws IOException{
        fleet.clear();
        for(int y = 0; y < status.level; y++){
            for(int x = 0; x <= 7; x++){
                alien = new Alien(settings);
                alien.rect.x = 30 + x*2*alien.rect.width;
                alien.rect.y = 30 + y*alien.rect.height;
                fleet.add(alien);
            }
        }
        settings.createFleet = false;
    }
    
    private void drawFleet(){
        fleet.stream().forEach((al) -> {
            al.execute(g);
        });
    }
    
    private void checkFleetBorder(){
        if(fleet.get(0).touch || fleet.get(fleet.size() -1).touch) changeFleet();
    }
    
    private void changeFleet(){
        fleet.stream().forEach((al) -> {
            al.changeDirection();
            al.goDown();
        });
    }
    
    private void newShoot(){
        bullet = new Bullet(ship, settings);
        bullets.add(bullet);
    }
    
    private void updateBullets(){
        for(Bullet bll : bullets){
            bll.shoot(g);
            if(!(bll.onScreen)){
                bulletIndex = bullets.indexOf(bll);
                out = true;
            }
        }
        
        if(out){
            removeBullet(bulletIndex);
            resetState();
        }
        
    }
    
    private void checkBulletAlien(){
        for(Bullet bll : bullets){
            for(Alien ali : fleet){
                if(bll.rect.intersects(ali.rect)){
                    alienIndex = fleet.indexOf(ali);
                    bulletIndex = bullets.indexOf(bll);
                    out = true;
                    status.value += status.level*10;
                    break;
                }
            }
        }
        
        if(out){
            removeAlien(alienIndex);
            removeBullet(bulletIndex);
            resetState();
        }
    }
    
    private void removeBullet(int index){
        bullets.remove(index);
    }
    
    private void removeAlien(int index){
        fleet.remove(index);
    }
    
    private void resetState(){
        alienIndex = 0;
        bulletIndex = 0;
        out = false;
    }
    
    private void checkAlienShip(){
        boolean fail = false;
        for(Alien all : fleet){
            if(all.rect.intersects(ship.rect)){
                fail = true;
            }
        }
        
        if(fail) restart();
    }
    
    
    private void restart(){
        status.chancesLeft--;
        settings.shoot = false;
        settings.start = false;
        settings.gameOver = true;
        if(status.chancesLeft == 0){
            status.level = 1;
            status.value = 0;
            status.chancesLeft = 3;
        }
        ship.center();
    }
    
    private void checkLevel(){
        if(fleet.isEmpty()){
            bullets.clear();
            settings.createFleet = true;
            settings.start = false;
            settings.preStart = true;
            status.level++;
        }
    }
}
