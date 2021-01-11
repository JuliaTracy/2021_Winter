function wuziqi
    axis equal
    axis([-10,10,-10,10])
    set(gca,'xtick',[],'ytick',[],'xcolor','w','ycolor','w')
    set(gca,'color',[0.8392,0.7216,0.3804])
    hold on
    row=19;col=19;
    x1=[-9,-9,-8,-8,-7,-7,-6,-6,-5,-5,-4,-4,-3,-3,-2,-2,-1,-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9];
    y1=[-9,9,9,-9,-9,9,9,-9,-9,9,9,-9,-9,9,9,-9,-9,9,9,-9,-9,9,9,-9,-9,9,9,-9,-9,9,9,-9,-9,9,9,-9,-9,9];
    x2=[-9,9,9,-9,-9];y2=[9,9,-9,-9,9];x3=[-9.2,9.2,9.2,-9.2,-9.2];y3=[9.2,9.2,-9.2,-9.2,9.2];x4=[-6,-6,-6,0,0,0,6,6,6];y4=[6,0,-6,6,0,-6,6,0,-6];
    plot(x1,y1,'k'),plot(y1,x1,'k'),plot(x2,y2,'k','LineWidth',2),plot(x3,y3,'k'),scatter(gca,x4,y4,30,'k','filled')
    win=0;control=1;postion=[0 0];
    black=[20,20];white=[-20,-20];
    black(1,:)=[];white(1,:)=[];
    plotblack=scatter(gca,black(:,1),black(:,2),150,'k','filled');
    plotwhite=scatter(gca,white(:,1),white(:,2),150,'w','filled');
    plotpostion=scatter(gca,postion(1,1),postion(1,2),150,'rx');
    set(gcf, 'KeyPressFcn', @key)  
    function wuziqigame(~,~)
        postion(postion>9)=-9;
        postion(postion<-9)=9;
        panding()
        set(plotblack,'XData',black(:,1),'YData',black(:,2))
        set(plotwhite,'XData',white(:,1),'YData',white(:,2))
        set(plotpostion,'XData',postion(1,1),'YData',postion(1,2))
           if win==1
                buttonName1=questdlg('black win. What do you mean to do?','black win','close','restart','close');
                if isempty(buttonName1),buttonName1='end';end
                if strcmp(buttonName1,'restart'),clf;wuziqi();
                else if strcmp(buttonName1,'close'),close;end
                end
            end
            if win==-1
                buttonName1=questdlg('white win. What do you mean to do?','white win','close','restart','close');
                if isempty(buttonName1),buttonName1='end';end
                if strcmp(buttonName1,'restart'),clf;wuziqi();
                else if strcmp(buttonName1,'close'),close;end
                end
            end
    end
    function panding(~,~)
        mat=zeros(row+4,col+4);
        x=3:(row+2);y=3:(col+2);
        qipan=zeros(row,col);
        blackpos=black(:,1)+10+(black(:,2)+10-1)*row;
        whitepos=white(:,1)+10+(white(:,2)+10-1)*row;
        qipan(blackpos)=1;qipan(whitepos)=-1;mat(x,y)=qipan;
        mat1=mat(x,y)+mat(x+1,y)+mat(x+2,y)+mat(x-1,y)+mat(x-2,y);
        mat2=mat(x,y)+mat(x,y+1)+mat(x,y+2)+mat(x,y-1)+mat(x,y-2);
        mat3=mat(x,y)+mat(x+1,y+1)+mat(x+2,y+2)+mat(x-1,y-1)+mat(x-2,y-2);
        mat4=mat(x,y)+mat(x+1,y-1)+mat(x+2,y-2)+mat(x-1,y+1)+mat(x-2,y+2);
        con=[mat1;mat2;mat3;mat4];con1=con==5;con2=con==-5;
        if (sum(sum(con1)))~=0,win=1;end
        if (sum(sum(con2)))~=0,win=-1;end      
    end
    function key(~,event)
        switch event.Key
            case 'uparrow',postion=postion+[0,1];
            case 'downarrow',postion=postion+[0,-1];
            case 'leftarrow',postion=postion+[-1,0];
            case 'rightarrow',postion=postion+[1,0];   
            case 'c',postion=[0,0];
            case 'space'
                if sum(ismember([black(:,1:2);white(:,1:2)],postion(1,1:2),'rows'))==0
                    if control==1,black=[black;postion];end
                    if control==0,white=[white;postion];end
                    control=mod(control+1,2);
                end
            case 'backspace'
                co=0;
                if control==0&&~isempty(black),black(end,:)=[];co=1;end
                if control==1&&~isempty(white),white(end,:)=[];co=1;end
                if co==1,control=mod(control+1,2);end
        end
        wuziqigame()
        end
end