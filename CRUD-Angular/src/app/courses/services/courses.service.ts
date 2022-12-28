import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { delay, Observable, tap } from 'rxjs';

import { Course } from '../interfaces/course';


@Injectable({
  providedIn: 'root'
})
export class CoursesService {

  private readonly API = 'api/courses';

  constructor(
    private httpClient: HttpClient
  ) { }

  list(): Observable<Course[]> {
    /*let list = [
        { "_id":"1", "name":"Angular + spring-boot", "category": "fullstack", "duracao": "46516" },
        { "_id":"2", "name":"Angular", "category": "front end", "duracao": "46516" },
        { "_id":"2", "name":"Spring-boot", "category": "back end", "duracao": "46516" }
      ]*/

    // return of (list);
    return this.httpClient.get<Course[]>(this.API).pipe(
      // delay(1000),
      tap(list => console.log(list))
    )
  }

  loadById(_id: string) {
    return this.httpClient.get<Course>(`${this.API}/${_id}`);
  }

  save(record: Partial<Course>) {
    if(record._id){
      console.log("updater", record);
      return this.update(record)
    }
    console.log("creater", record);
    return this.create(record)
  }

  private create(record: Partial<Course>){
    return this.httpClient.post<Course>(this.API, record);

  }

  private update(record: Partial<Course>){
    return this.httpClient.put<Course>(`${this.API}/${record._id}`, record);

  }

  public delete(_id: string){
    return this.httpClient.delete(`${this.API}/${_id}`);

  }

}
