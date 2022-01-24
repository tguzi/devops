<template>
  <el-container class="layout-container">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
      <el-scrollbar>
        <el-menu :default-openeds="['1', '3']">
          <el-sub-menu index="1">
            <template #title>
              <el-icon><IconMenu /></el-icon>导航
            </template>
            <el-menu-item-group>
              <el-menu-item>分支流水</el-menu-item>
            </el-menu-item-group>
          </el-sub-menu>
        </el-menu>
      </el-scrollbar>
    </el-aside>

    <el-container>
      <el-header style="text-align: right; font-size: 12px">
        <div class="toolbar">
          <el-dropdown>
            <el-icon style="margin-right: 8px; margin-top: 1px"><setting /></el-icon>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>查看</el-dropdown-item>
                <el-dropdown-item>退出</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
          <span>用户名</span>
        </div>
      </el-header>
      <el-main>
        <el-scrollbar>
          <el-row :gutter="12">
            <el-col :span="8">
              <el-card shadow="always">测试环境</el-card>
            </el-col>
            <el-col :span="8">
              <el-card shadow="always">预发环境</el-card>
            </el-col>
            <el-col :span="8">
              <el-card shadow="always">线上环境</el-card>
            </el-col>
          </el-row>
        </el-scrollbar>
      </el-main>
    </el-container>
  </el-container>
</template>

<script lang="ts" setup>
  import { ref } from 'vue'
  import { Menu as IconMenu, Setting } from '@element-plus/icons-vue'
</script>

<style lang="less" scope>
  .layout-container {
    width: 100vw;
    height: 100vh;
    box-sizing: border-box;
    overflow: hidden;
    .el-header {
      position: relative;
      background-color: #b3c0d1;
      color: var(--el-text-color-primary);
    }
    .el-aside {
      width: 240px;
      color: var(--el-text-color-primary);
      background: #fff !important;
      border-right: solid 1px #e6e6e6;
      box-sizing: border-box;
    }
    .el-menu {
      border-right: none;
    }
    .el-main {
      padding: 0;
    }
    .toolbar {
      position: absolute;
      display: inline-flex;
      align-items: center;
      top: 50%;
      right: 20px;
      transform: translateY(-50%);
    }
  }
</style>
