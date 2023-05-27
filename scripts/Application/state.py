# coding: UTF-8

from typing import Callable

class State:
    def __init__(self, value):
        self.__value = value
        self.__observer = Observer()
    
    def get(self):
        return self.__value
    
    def set(self, value) -> None:
        if self.__value != value:
            self.__value = value
            
            # value 変更時に各observerに通知
            self.__observer.notify()
                
    def bind(self, callback: Callable[ [], None ]) -> None:
        self.__observer.bind(callback)

class Observer:
    def __init__(self):
        self.__observers = []
        
    def bind(self, callback: Callable[ [], None ]) -> None:
        self.__observers.append(callback)
    
    def notify(self):
        for callback in self.__observers:
            callback()

