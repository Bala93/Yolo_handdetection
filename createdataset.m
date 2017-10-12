function createdataset()

path = '/home/balamurali/Downloads/hand_dataset/validation_dataset/validation_data/';
path_ = [path 'images/*.jpg'];
uf = dir(path_);
size(uf)

for i = 1:length(uf)
    
    
    dot = strfind(uf(i).name,'.');
    imname = uf(i).name(1:dot-1);
    
    load([path 'annotations/' imname '.mat']);
    im = imread([path 'images/' uf(i).name]);
    annot_filename = [path 'yoloannotation/',imname,'.txt'];
    ann_data = fopen(annot_filename,'w');
    [imgw,imgh] = size(im);
%     imshow(im);
    
    for j = 1:length(boxes)
        box = boxes{j};
        
        %line([box.a(2) box.b(2)]',[box.a(1) box.b(1)]','LineWidth',3,'Color','y');
%         line([box.b(2) box.c(2) box.d(2) box.a(2)]',[box.b(1) box.c(1) box.d(1) box.a(1)]','LineWidth',3,'Color','r');
        x_ = [box.b(2) box.c(2) box.d(2) box.a(2)];
        y_ = [box.b(1) box.c(1) box.d(1) box.a(1)];
        
        x1  = min(x_);
        y1  = min(y_);
        x2  = max(x_);
        y2  = max(y_);
        
        bound_w = x2 - x1;
        bound_h = y2 - y1;
        
%         line([box.b(2) box.c(2) box.d(2) box.a(2)]',[box.b(1) box.c(1) box.d(1) box.a(1)]','LineWidth',3,'Color','r');
%         line([box.b(2) box.c(2) box.d(2) box.a(2)]',[box.b(1) box.c(1) box.d(1) box.a(1)]','LineWidth',3,'Color','r');
%         rectangle('Position',[x1,y1,bound_w,bound_h],'LineWidth',3,'EdgeColor','r');
        lable_text =[num2str(1) ' ' num2str(x1/imgw) ' ' num2str(y1/imgh) ' ' num2str(bound_w/imgw) ' ' num2str(bound_h/imgh)];
        lable_text = [lable_text '\n'];
        fprintf(ann_data,lable_text);
%         break
    end
    fclose(ann_data);
%     disp('Press any key to move onto the next image');pause;
%     break
    
end