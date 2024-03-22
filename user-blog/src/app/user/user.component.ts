import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {

  users: any;

  constructor(private service:UserService) {  }

  ngOnInit(): void {
    this.users = this.service.getUsers().subscribe(data=>this.users=data);
  }
}
