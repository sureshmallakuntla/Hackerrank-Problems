# SQL Project planning

Select min(start_date), max(end_date)
From (
    Select p.*, 
        if(isnull(prev.End_Date), @pc:=@pc+1, @pc) as project_counter
    From Projects p
        left join Projects prev on p.Start_Date = prev.End_Date
        join (SELECT @pc:=0) as t
    ) as tt
Group by project_counter
Order by count(*),min(start_date)
