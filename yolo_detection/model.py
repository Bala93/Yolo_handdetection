#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:14:55 2017

@author: balamurali
"""
import torch
import torch.nn as nn
from torch.autograd import Variable

class Yolo(nn.Module):
    def __init__(self):
        super(Yolo,self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3,out_channels=32,kernel_size=3,padding=1,stride=1)
        self.mp1   = nn.MaxPool2d(kernel_size=2,stride=2)
        
        self.conv2 = nn.Conv2d(in_channels=32,out_channels=64,kernel_size=3,padding=1,stride=1)
        self.mp2   = nn.MaxPool2d(kernel_size=2,stride=2)
        
        self.conv3 = nn.Conv2d(in_channels=64,out_channels=128,kernel_size=3,padding=1,stride=1)
        self.conv4 = nn.Conv2d(in_channels=128,out_channels=64,kernel_size=1,padding=1,stride=1)
        self.conv5 = nn.Conv2d(in_channels=64,out_channels=128,kernel_size=3,padding=1,stride=1)
        self.mp3   = nn.MaxPool2d(kernel_size=2,stride=2)
        
        self.conv6 = nn.Conv2d(in_channels=128,out_channels=256,kernel_size=3,padding=1,stride=1)
        self.conv7 = nn.Conv2d(in_channels=256,out_channels=128,kernel_size=1,padding=1,stride=1)
        self.conv8 = nn.Conv2d(in_channels=128,out_channels=256,kernel_size=3,padding=1,stride=1)
        self.mp4   = nn.MaxPool2d(kernel_size=2,stride=2)
        
        self.conv9 = nn.Conv2d(in_channels=256,out_channels=512,kernel_size=3,padding=1,stride=1)
        self.conv10 = nn.Conv2d(in_channels=512,out_channels=256,kernel_size=1,padding=1,stride=1)
        self.conv11 = nn.Conv2d(in_channels=256,out_channels=512,kernel_size=3,padding=1,stride=1)
        self.conv12 = nn.Conv2d(in_channels=512,out_channels=256,kernel_size=1,padding=1,stride=1)
        self.conv13 = nn.Conv2d(in_channels=256,out_channels=512,kernel_size=3,padding=1,stride=1)
        self.mp5    = nn.MaxPool2d(kernel_size=2,stride=2)
        
        self.conv14 = nn.Conv2d(in_channels=512,out_channels=1024,kernel_size=3,padding=1,stride=1)
        self.conv15 = nn.Conv2d(in_channels=1024,out_channels=512,kernel_size=1,padding=1,stride=1)
        self.conv16 = nn.Conv2d(in_channels=512,out_channels=1024,kernel_size=3,padding=1,stride=1)
        self.conv17 = nn.Conv2d(in_channels=1024,out_channels=512,kernel_size=1,padding=1,stride=1)
        self.conv18 = nn.Conv2d(in_channels=512,out_channels=1024,kernel_size=3,padding=1,stride=1)
        self.conv19 = nn.Conv2d(in_channels=1024,out_channels=1024,kernel_size=3,padding=1,stride=1)
        self.conv20 = nn.Conv2d(in_channels=1024,out_channels=1024,kernel_size=3,padding=1,stride=1)
        self.conv21 = nn.Conv2d(in_channels=1024,out_channels=64,kernel_size=1,padding=1,stride=1)
        self.conv22 = nn.Conv2d(in_channels=64,out_channels=1024,kernel_size=3,padding=1,stride=1)
        self.conv23 = nn.Conv2d(in_channels=1024,out_channels=30,kernel_size=1,padding=1,stride=1)
    
    def forward(self,x):
        print 1,x.size()
        x = self.conv1(x)
        print 2,x.size()        
        x = self.mp1(x)
        print 3,x.size()        
        x = self.conv2(x)
        print 4,x.size()
        x = self.mp2(x)
        print 5,x.size()        
        x = self.conv3(x)
        print 6,x.size()
        x = self.conv4(x)
        print 7,x.size()
        x = self.conv5(x)
        print 8,x.size()
        x = self.mp3(x)
        print 9,x.size()
        x = self.conv6(x)
        print 10,x.size()
        x = self.conv7(x)
        print 11,x.size()
        x = self.conv8(x)
        print 12,x.size()
        x = self.mp4(x)
        print 13,x.size()
        x = self.conv9(x)
        print 14,x.size()
        x = self.conv10(x)
        print 15,x.size()
        x = self.conv11(x)
        print 16,x.size()
        x = self.conv12(x)
        print 17,x.size()
        x = self.conv13(x)
        print 18,x.size()
        x = self.mp5(x)
        print 19,x.size()
        x = self.conv14(x)
        print 20,x.size()
        x = self.conv15(x)
        print 21,x.size()
        x = self.conv16(x)
        print 22,x.size()
        x = self.conv17(x)
        print 23,x.size()
        x = self.conv18(x)
        print 24,x.size()
        x = self.conv19(x)
        print 25,x.size()
        x = self.conv20(x)
        print 26,x.size()
        x = self.conv21(x)
        print 27,x.size()
        x = self.conv22(x)
        print 28,x.size()
        x = self.conv23(x)
        print 29,x.size()
        return x
    
net = Yolo()
inp = Variable(torch.rand([1,3,416,416]))
out = net(inp)
#print out.size()