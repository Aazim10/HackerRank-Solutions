SELECT  S.name FROM STUDENTS S 
WHERE S.MARKS>75
ORDER BY substr(S.name,length(name)-2,3), ID;
